import pandas as pd


def get_appearances(location='', apply_func=lambda x: x):
    return apply_func(pd.read_csv(location + 'Assignment_Data_2023-2024/appearances.csv'))


def get_club_games(location=''):
    return pd.read_csv(location + 'Assignment_Data_2023-2024/club_games.csv')


def get_clubs(location=''):
    return pd.read_csv(location + 'Assignment_Data_2023-2024/clubs.csv')


def get_competitions(location=''):
    return pd.read_csv(location + 'Assignment_Data_2023-2024/competitions.csv')


def get_game_events(location=''):
    return pd.read_csv(location + 'Assignment_Data_2023-2024/game_events.csv')


def get_game_lineups(location=''):
    return pd.read_csv(location + 'Assignment_Data_2023-2024/game_lineups.csv')


def get_games(location=''):
    return pd.read_csv(location + 'Assignment_Data_2023-2024/games.csv')


def get_player_valuations(location=''):
    return pd.read_csv(location + 'Assignment_Data_2023-2024/player_valuations.csv')


def get_players(location=''):
    return pd.read_csv(location + 'Assignment_Data_2023-2024/players.csv')


def clean_appearances(appearances, games, location=''):
    if appearances is not None and games is not None:
        appearances['appearance_id'] = appearances['appearance_id'].astype('string')
        appearances['player_name'] = appearances['player_name'].astype('string')
        appearances['competition_id'] = appearances['competition_id'].astype('string')
        appearances['date'] = pd.to_datetime(appearances['date'].astype('string'))
        appearances['red_cards'] = (appearances['red_cards'].apply(lambda x: bool(x))).astype('bool')
        players = get_players(location)
        appearances_to_drop = appearances.query('player_id not in @players["player_id"]', engine="python")
        appearances = appearances.drop(appearances_to_drop.index.tolist(), axis=0)
        players = None
        appearances_to_drop = None
        # Removing games with no match
        appearances = appearances[appearances['game_id'].isin(games['game_id'])]
        appearances.rename(columns={'date': 'game_date'}, inplace=True)
    else:
        print('Error occurred reading "appearances" dataset')
    return appearances


def clean_club_games(club_games, location=''):
    cleaned_games = None
    if club_games is not None:
        club_games = club_games.drop(columns=['opponent_id', 'opponent_goals', 'opponent_position',
                                              'opponent_manager_name'])
        club_games.loc[club_games['own_position'].isnull(), 'own_position'] = -1
        club_games['own_position'] = club_games['own_position'].astype('int')
        club_games['own_manager_name'] = club_games['own_manager_name'].astype('string')
        club_games['hosting'] = (club_games['hosting'].apply(lambda x: bool(x.__str__() == 'Home'))).astype('bool')
        club_games['is_win'] = (club_games['is_win'].apply(lambda x: bool(x == 1))).astype('bool')
        games = get_games(location)
        games_subset_1 = games[['game_id', 'home_club_id', 'home_club_formation']].copy()
        games_subset_2 = games[['game_id', 'away_club_id', 'away_club_formation']].copy()
        games_subset_1 = games_subset_1.rename(columns={'home_club_id': 'club_id',
                                                        'home_club_formation': 'club_formation'})
        games_subset_2 = games_subset_2.rename(columns={'away_club_id': 'club_id',
                                                        'away_club_formation': 'club_formation'})
        game_subset = pd.concat([games_subset_1, games_subset_2], axis=0)
        games_subset_1 = None
        games_subset_2 = None
        club_games = pd.merge(club_games, game_subset, on=['game_id', 'club_id'])
        club_games['club_formation'] = club_games['club_formation'].astype('string')
        games_subset = None

        # finding inconsistent tuples in club_games
        missing_club_cg = club_games[~club_games['club_id'].isin(clean_clubs(get_clubs(location))['club_id'])]

        # saving game_id's to drop
        cg_ids_to_drop = club_games.query('game_id.isin(@missing_club_cg["game_id"])', engine='python')['game_id']
        missing_club_cg = None
        club_games = club_games[~club_games['game_id'].isin(cg_ids_to_drop)]
        cg_to_drop = None
        cleaned_games = clean_games(games)
        cleaned_games = cleaned_games[cleaned_games['game_id'].isin(club_games['game_id'])]
        games = None
    else:
        print('Error occurred reading "club_games" dataset')
    return [club_games, cleaned_games]


def clean_clubs(clubs):
    if clubs is not None:
        clubs = clubs.drop(columns=['coach_name', 'total_market_value', 'club_code', 'url'])  # Both are null
        clubs['name'] = clubs['name'].astype('string')
        clubs['name'] = clubs['name'].str.replace('"', "'", regex=False)
        clubs['name'] = clubs['name'].str.replace('Football Club', "FC", regex=False)
        clubs['domestic_competition_id'] = clubs['domestic_competition_id'].astype('string')
        # If squad_size == 0 -> The club could not exist anymore. We have not touched these value.
        clubs.fillna({'foreigners_percentage': 0}, inplace=True)
        clubs['foreigners_percentage'] = clubs['foreigners_percentage'].astype('int')
        clubs['stadium_name'] = clubs['stadium_name'].astype('string')
        clubs.at[409, 'stadium_seats'] = 4851  # correcting the only 0 value!
        clubs['net_transfer_record'] = clubs['net_transfer_record'].astype('string')
        clubs['net_transfer_record'] = (clubs['net_transfer_record'].apply(clean_net_records)).astype('int')
        clubs.rename(columns={'name': 'club_name', 'domestic_competition_id': 'local_competition_code'}, inplace=True)
    else:
        print('Error occurred reading "clubs" dataset')
    return clubs


def clean_net_records(x):
    if x != x or len(x) == 0:
        return -1
    if '€' in x:
        x = (x[1:] if x[0] == '€' else x[2:])
    else:
        return 0
    value = float(x[:-1])
    if value != value:
        raise Exception('Value wrongly set!')
    if 'm' in x:
        value *= 1_000_000
    elif 'k' in x:
        value *= 1000
    value = int(value)
    if value % 2 != 0:
        value = (value + 1 if value > 0 else value - 1)
    return int(value)


def clean_competitions(competitions):
    if competitions is not None:
        competitions = competitions.drop(columns=['competition_code', 'country_id', 'confederation', 'url'])
        # the following competition has no game in dataset
        competitions = competitions[competitions['competition_id'] != "KLUB"]
        # Casting types
        competitions['competition_id'] = competitions['competition_id'].astype('string')
        competitions['name'] = competitions['name'].astype('string')
        competitions['sub_type'] = competitions['sub_type'].astype('string')
        competitions['type'] = competitions['type'].astype('string')
        competitions['country_name'] = competitions['country_name'].astype('string')
        competitions['domestic_league_code'] = competitions['domestic_league_code'].astype('string')
        # Renaming columns
        competitions.rename(columns={'name': 'competition_name', 'type': 'competition_type'}, inplace=True)
    else:
        print('Error occurred reading "competitions" dataset')
    return competitions


def format_string(des_elem=''):
    # pre: des_elem is not None
    if des_elem is not None and len(des_elem) > 0:
        for i in range(0, len(des_elem) - 1):
            # print(f'i= {i}, len= {len(des_elem)}')
            if des_elem[i].isdigit():
                if des_elem[i] == '1' and des_elem[i + 1] == '.':
                    des_elem = des_elem[:i + 1] + 'st' + des_elem[i + 2:]
                    i = i + 2
                elif des_elem[i] == '2' and des_elem[i + 1] == '.':
                    des_elem = des_elem[:i + 1] + 'nd' + des_elem[i + 2:]
                    i = i + 2
                elif des_elem[i] == '3' and des_elem[i + 1] == '.':
                    des_elem = des_elem[:i + 1] + 'rd' + des_elem[i + 2:]
                    i = i + 2
                else:
                    while i < len(des_elem) and des_elem[i].isdigit():
                        i = i + 1
                    if i < len(des_elem) and des_elem[i] == '.':
                        des_elem = des_elem[:i] + 'th' + des_elem[i + 1:]
                        i = i + 2
        return des_elem
    return des_elem


def clean_game_events(game_events, games, location=''):
    if game_events is not None or games is not None:
        # Removing unnecessary columns and values
        game_events = game_events.drop(columns=['date'])

        # Formatting description
        game_events['description'].replace([float('NaN'), ', Not reported'], None, inplace=True)
        target = game_events['description'].apply(lambda x: x if x is None else x[2:] if x[0] == ',' else x)
        target = target.apply(format_string)
        game_events['description'].update(target)
        target = None

        # Formatting player_in_id
        game_events.fillna({'player_in_id': -1, 'player_assist_id': -1}, inplace=True)

        # Casting types
        game_events['game_event_id'] = game_events['game_event_id'].astype('string')
        game_events['type'] = game_events['type'].astype('string')
        game_events['description'] = game_events['description'].astype('string')
        game_events['player_in_id'] = game_events['player_in_id'].astype('int')
        game_events['player_assist_id'] = game_events['player_assist_id'].astype('int')

        # Checking foreign keys, removing game and player ids with no match
        game_events = game_events[game_events['game_id'].isin(games['game_id'])]
        game_events = game_events[game_events['player_id'].isin(clean_players(get_players(location))['player_id'])]

        # Renaming columns
        game_events.rename(columns={'type': 'event_type', 'description': 'event_description'}, inplace=True)
    else:
        print('Error occurred reading "game_events" dataset')
    return game_events


def clean_game_lineups(game_lineups, games):
    if game_lineups is not None and games is not None:
        game_lineups['game_lineups_id'] = game_lineups['game_lineups_id'].astype('string')
        game_lineups['type'] = game_lineups['type'].astype('string')
        game_lineups['number'].replace('-', -1, inplace=True)
        game_lineups['number'] = game_lineups['number'].astype('int')
        # players are not consistent with the player_id
        game_lineups['player_name'] = game_lineups['player_name'].astype('string')
        game_lineups['team_captain'] = game_lineups['team_captain'].astype('bool')
        game_lineups['position'] = game_lineups['position'].astype('string')
        game_lineups['position'].replace('midfield', 'Midfield', inplace=True)
        # Removing games with no match
        game_lineups = game_lineups[game_lineups['game_id'].isin(games['game_id'])]
    else:
        print('Error occurred reading "game_lineups" dataset')
    return game_lineups


def clean_games(games):
    if games is not None:
        games.drop(columns=['home_club_id', 'away_club_id', 'home_club_goals', 'away_club_goals', 'home_club_position',
                            'away_club_position', 'home_club_manager_name', 'away_club_manager_name',
                            'home_club_formation', 'away_club_formation', 'home_club_name', 'away_club_name',
                            'competition_type', 'aggregate', 'url'], inplace=True)
        games.replace(float('NaN'), None, inplace=True)
        games['competition_id'] = games['competition_id'].astype('string')
        games['round'] = games['round'].astype('string')
        games['round'] = (games['round'].apply(format_string)).astype('string')
        games['date'] = pd.to_datetime(games['date'].astype('string'))
        games['stadium'] = games['stadium'].astype('string')
        games['attendance'].fillna(-1, inplace=True)
        games['attendance'] = games['attendance'].astype('int')
        games['referee'] = games['referee'].astype('string')
        games.rename({'date': 'game_date'}, inplace=True)
    else:
        print('Error occurred reading "games" dataset')
    return games


def clean_player_valuations(player_valuations):
    if player_valuations is not None:
        player_valuations.drop(columns=['datetime', 'n'], inplace=True)
        # Todo complete this function
        player_valuations['last_season'] = player_valuations['last_season'].astype('int')
        player_valuations['date'] = pd.to_datetime(player_valuations['date'].astype('string'))
        player_valuations['dateweek'] = pd.to_datetime(player_valuations['dateweek'].astype('string'))
        player_valuations['player_club_domestic_competition_id'] = (
            player_valuations['player_club_domestic_competition_id'].astype('string'))
        # Renaming columns
        player_valuations.rename(columns={'dateweek': 'date_week',
                                          'player_club_domestic_competition_id': 'current_dom_competition_code',
                                          'market_value_in_eur': 'market_value_eur'}, inplace=True)
    else:
        print('Error occurred reading "player_valuations" dataset')
    return player_valuations


def clean_players(players):
    if players is not None:
        players.drop(columns=['first_name', 'player_code', 'current_club_name',
                              'current_club_domestic_competition_id', 'url'], inplace=True)
        players.replace(float('NaN'), None, inplace=True)
        players['name'] = players['name'].astype('string')
        players['last_name'] = players['last_name'].astype('string')
        players['country_of_birth'] = players['country_of_birth'].astype('string')
        players['city_of_birth'] = players['city_of_birth'].astype('string')
        players['country_of_citizenship'] = players['country_of_citizenship'].astype('string')
        players['date_of_birth'] = pd.to_datetime(players['date_of_birth'].astype('string'))
        players['sub_position'] = players['sub_position'].astype('string')
        players['position'] = (players['position'].replace('Missing', None)).astype('string')
        players['foot'] = players['foot'].astype('string')
        # Filling NA values with -1 where needed
        players[['height_in_cm', 'market_value_in_eur', 'highest_market_value_in_eur']] = (
            players[['height_in_cm', 'market_value_in_eur', 'highest_market_value_in_eur']].fillna(-1))
        players['height_in_cm'] = ((players['height_in_cm'].apply(lambda x: x if x == -1 or x >= 100 else x * 10))
                                   .astype('int'))
        players['market_value_in_eur'] = players['market_value_in_eur'].astype('int')
        players['highest_market_value_in_eur'] = players['highest_market_value_in_eur'].astype('int')
        players['contract_expiration_date'] = pd.to_datetime(players['contract_expiration_date'].astype('string'))
        players['agent_name'] = players['agent_name'].astype('string')
        players['image_url'] = players['image_url'].astype('string')
        # Renaming columns
        players.rename(columns={'name': 'player_name', 'type': 'player_type', 'market_value_in_eur': 'value_eur',
                                'highest_market_value_in_eur': 'top_value_eur'}, inplace=True)
    else:
        print('Error occurred reading "players" dataset')
    return players


def create_flags(loc=''):
    """
    It creates a DataFrame with 3 fields: domestic_league_code, country_name and flag_url
        :return: the DataFrame of flags with their codes and names
    """
    competitions = clean_competitions(get_competitions(loc))
    nations = (competitions[['domestic_league_code', 'country_name']].
               drop_duplicates().query('not domestic_league_code.isnull()', engine='python')).reset_index(drop=True)
    competitions = None
    flag_series = pd.Series([
        'https://raw.githubusercontent.com/lipis/flag-icons/05059f9cde4a872f1692cb017abb1140e9aceae9/flags/4x3/it.svg',
        'https://raw.githubusercontent.com/lipis/flag-icons/05059f9cde4a872f1692cb017abb1140e9aceae9/flags/4x3/nl.svg',
        'https://raw.githubusercontent.com/lipis/flag-icons/05059f9cde4a872f1692cb017abb1140e9aceae9/flags/4x3/gr.svg',
        'https://raw.githubusercontent.com/lipis/flag-icons/05059f9cde4a872f1692cb017abb1140e9aceae9/flags/4x3/pt.svg',
        'https://raw.githubusercontent.com/lipis/flag-icons/05059f9cde4a872f1692cb017abb1140e9aceae9/flags/4x3/ru.svg',
        'https://raw.githubusercontent.com/lipis/flag-icons/05059f9cde4a872f1692cb017abb1140e9aceae9/flags/4x3/es.svg',
        'https://raw.githubusercontent.com/lipis/flag-icons/05059f9cde4a872f1692cb017abb1140e9aceae9/flags/4x3/dk.svg',
        'https://raw.githubusercontent.com/lipis/flag-icons/05059f9cde4a872f1692cb017abb1140e9aceae9/flags/4x3/fr.svg',
        'https://raw.githubusercontent.com/lipis/flag-icons/05059f9cde4a872f1692cb017abb1140e9aceae9/flags/4x3/be.svg',
        'https://raw.githubusercontent.com/lipis/flag-icons/05059f9cde4a872f1692cb017abb1140e9aceae9/flags/4x3/gb.svg',
        'https://raw.githubusercontent.com/lipis/flag-icons/05059f9cde4a872f1692cb017abb1140e9aceae9/flags/4x3/ua.svg',
        'https://raw.githubusercontent.com/lipis/flag-icons/05059f9cde4a872f1692cb017abb1140e9aceae9/flags/4x3/tr.svg',
        'https://raw.githubusercontent.com/lipis/flag-icons/05059f9cde4a872f1692cb017abb1140e9aceae9/flags/4x3/de.svg',
        'https://raw.githubusercontent.com/lipis/flag-icons/05059f9cde4a872f1692cb017abb1140e9aceae9/flags/4x3/gb-sct'
        '.svg',
    ]).rename('flag_url', axis=0).astype('string')
    nations = nations.join(flag_series, how='outer')
    flag_series = None
    return nations
