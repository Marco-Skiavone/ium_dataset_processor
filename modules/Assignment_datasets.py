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
    appearance['date'] = pd.to_datetime(appearance['date'])
    appearance['competition_id'] = appearance['competition_id'].astype('string')
    appearance.dropna(inplace=True)  # @Todo uncompleted
    return appearance


def clean_club_games(club_games):
    club_games = club_games[['game_id', 'club_id', 'own_goals', 'own_position',
                             'own_manager_name', 'hosting', 'is_win']]
    club_games['own_position'] = club_games['own_position'].apply(lambda x: int(-1 if x != x else int(x)))
    club_games['own_manager_name'] = club_games['own_manager_name'].astype('string')
    club_games['hosting'] = club_games['hosting'].apply(lambda x: bool(x.__str__() == 'Home'))
    club_games['is_win'] = club_games['is_win'].apply(lambda x: bool(x == 1))

    # @Todo Here we have to add 'club_formation' column from games!
    # club_formation is divided into 2 columns: home_c. and away_c.
    # Every club_games tuple is linked up to only 1 value.
    return club_games


def clean_clubs(clubs):
    clubs = clubs.drop(columns=['coach_name', 'total_market_value', 'club_code'])    # Both are null
    clubs['name'] = clubs['name'].astype('string')
    clubs['domestic_competition_id'] = clubs['domestic_competition_id'].astype('string')

    # @Todo 1. resolve squad == 0;
    # players = get_players()
    # clubs['squad_size'] = clubs['squad_size'].apply(lambda x: search_squad_players(x, players))
    # players = None
    # @Todo 2. resolve foreigners percentage when Nan;
    # clubs['foreigners_percentage'] = clubs['foreigners_percentage'].apply(lambda x: )
    clubs['stadium_name'] = clubs['stadium_name'].astype('string')
    clubs.at[409, 'stadium_seats'] = 4851       # correcting the only 0 value!

    clubs['url'] = clubs['url'].astype('string')
    # @Todo still everything WIP here!
    clubs.rename(columns={'name': 'club_name', 'domestic_competition_id': 'local_competition_code', 'url': 'club_url'},
                 inplace=True)
    return clubs


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


def clean_game_events(game_events):
    game_events = game_events.drop(columns=['date'])
    # Casting types
    game_events['game_event_id'] = game_events['game_event_id'].astype('string')
    game_events['type'] = game_events['type'].astype('string')
    game_events['description'] = game_events['description'].astype('string')
    game_events['player_in_id'] = game_events['player_in_id'].astype('int')
    game_events['player_assist_id'] = game_events['player_assist_id'].astype('int')
    # @Todo Fixing 'description'

    game_events.rename(columns={'type': 'game_event_type'}, inplace=True)
    return game_events
