import pandas as pd


def get_appearance(location='', apply_func=lambda x: x):
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


def clean_appearance(appearance):
    appearance = appearance.drop(columns=['date', 'player_name', 'competition_id'])
    appearance['appearance_id'] = appearance['appearance_id'].astype('string')
    appearance['red_cards'] = (appearance['red_cards'].apply(lambda x: bool(x))).astype('bool')
    players = get_players()
    appearance_to_drop = appearance.query('player_id not in @players["player_id"]', engine="python")
    appearance = appearance.drop(appearance_to_drop.index.tolist(), axis=0)
    players = None
    appearance_to_drop = None
    return appearance


def clean_club_games(club_games):
    club_games = club_games.drop(columns=['opponent_id', 'opponent_goals', 'opponent_position',
                                          'opponent_manager_name'])
    club_games.loc[club_games['own_position'].isnull(), 'own_position'] = -1
    club_games['own_position'] = club_games['own_position'].astype('int')
    club_games['own_manager_name'] = club_games['own_manager_name'].astype('string')
    club_games['hosting'] = (club_games['hosting'].apply(lambda x: bool(x.__str__() == 'Home'))).astype('bool')
    club_games['is_win'] = (club_games['is_win'].apply(lambda x: bool(x == 1))).astype('bool')
    games = get_games()
    games_subset_1 = games[['game_id', 'home_club_id', 'home_club_formation']].copy()
    games_subset_2 = games[['game_id', 'away_club_id', 'away_club_formation']].copy()
    games_subset_1 = games_subset_1.rename(columns={'home_club_id': 'club_id', 'home_club_formation': 'club_formation'})
    games_subset_2 = games_subset_2.rename(columns={'away_club_id': 'club_id', 'away_club_formation': 'club_formation'})
    game_subset = pd.concat([games_subset_1, games_subset_2], axis=0)
    games_subset_1 = None
    games_subset_2 = None
    club_games = pd.merge(club_games, game_subset, on=['game_id', 'club_id'])
    games_subset = None
    games = None
    return club_games


def clean_clubs(clubs):
    clubs = clubs.drop(columns=['coach_name', 'total_market_value', 'club_code'])    # Both are null
    clubs['name'] = clubs['name'].astype('string')
    clubs['domestic_competition_id'] = clubs['domestic_competition_id'].astype('string')
    # If squad_size == 0 -> The club could not exist anymore. We have not touched these value.
    clubs.fillna({'foreigners_percentage': 0}, inplace=True)
    clubs['foreigners_percentage'] = clubs['foreigners_percentage'].astype('int')
    clubs['stadium_name'] = clubs['stadium_name'].astype('string')
    clubs.at[409, 'stadium_seats'] = 4851       # correcting the only 0 value!
    clubs['net_transfer_record'] = clubs['net_transfer_record'].astype('string')
    clubs['net_transfer_record'] = (clubs['net_transfer_record'].apply(clean_net_records)).astype('int')
    clubs['url'] = clubs['url'].astype('string')
    clubs.rename(columns={'name': 'club_name', 'domestic_competition_id': 'local_competition_code', 'url': 'club_url'},
                 inplace=True)
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
    competitions = competitions.drop(columns=['competition_code', 'country_id', 'confederation'])
    # Casting types
    competitions['competition_id'] = competitions['competition_id'].astype('string')
    competitions['name'] = competitions['name'].astype('string')
    competitions['sub_type'] = competitions['sub_type'].astype('string')
    competitions['type'] = competitions['type'].astype('string')
    competitions['country_name'] = competitions['country_name'].astype('string')
    competitions['domestic_league_code'] = competitions['domestic_league_code'].astype('string')
    competitions['url'] = competitions['url'].astype('string')
    # Renaming columns
    competitions.rename(columns={'name': 'competition_name', 'type': 'competition_type', 'url': 'competition_url'},
                        inplace=True)
    return competitions


def format_description(description_value=''):
    if description_value is not None:
        description_list = description_value.split(', ')
        return [format_string(des_elem) for des_elem in description_list]
    else:
        return description_value


def format_string(des_elem=''):
    # pre: des_elem is not None
    if des_elem[0].isdigit():
        substr = des_elem.split(".")
        if substr[0][0] == '1':
            substr[0] = substr[0] + 'st'
        elif substr[0][0] == '2':
            substr[0] = substr[0] + 'nd'
        elif substr[0][0] == '2':
            substr[0] = substr[0] + 'rd'
        else:
            substr[0] = substr[0] + 'th'
        return ''.join(substr)
    return des_elem


def clean_game_events(game_events):
    if game_events is not None:
        # Removing unnecessary columns and values
        game_events = game_events.drop(columns=['date'])

        # Formatting description
        game_events['description'].replace([float('NaN'), ', Not reported'], None, inplace=True)
        target = game_events['description'].apply(lambda x: x if x is None else x[2:] if x[0] == ',' else x)
        target = target.apply(format_description)
        game_events['description'].update(target)

        # Formatting player_in_id
        game_events.fillna({'player_in_id': -1, 'player_assist_id': -1}, inplace=True)

        # Casting types
        game_events['game_event_id'] = game_events['game_event_id'].astype('string')
        game_events['type'] = game_events['type'].astype('string')
        game_events['description'] = game_events['description'].astype('string')
        game_events['player_in_id'] = game_events['player_in_id'].astype('int')
        game_events['player_assist_id'] = game_events['player_assist_id'].astype('int')


        # Renaming columns
        game_events.rename(columns={'type': 'event_type',
                                    'description': 'event_description'},
                           inplace=True)
        return game_events
    print('Error occurred reading game_events dataset')
    return None


def clean_game_lineups(game_lineups):
    game_lineups['game_lineups_id'] = game_lineups['game_lineups_id'].astype('string')
    game_lineups['type'] = game_lineups['type'].astype('string')
    game_lineups['number'].replace('-', -1, inplace=True)
    game_lineups['number'] = game_lineups['number'].astype('int')
    # players are not consistent with the player_id
    game_lineups['player_name'] = game_lineups['player_name'].astype('string')
    game_lineups['team_captain'] = game_lineups['team_captain'].astype('bool')
    game_lineups['position'] = game_lineups['position'].astype('string')
    game_lineups['position'].replace('midfield', 'Midfield', inplace=True)
    return game_lineups
