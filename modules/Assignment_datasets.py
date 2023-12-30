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
    appearance.dropna(inplace=True)  # @Todo uncomplete
    return appearance


def clean_club_games(club_games):
    club_games = club_games[['game_id', 'club_id', 'own_goals', 'own_position',
                             'own_manager_name', 'hosting', 'is_win']]
    club_games['own_position'] = club_games['own_position'].apply(lambda x: int(-1 if x != x else int(x)))
    club_games['own_manager_name'] = club_games['own_manager_name'].astype('string')
    club_games['hosting'] = club_games['hosting'].apply(lambda x: bool(x.__str__() == 'Home'))
    club_games['is_win'] = club_games['is_win'].apply(lambda x: bool(x == 1))
    # @Todo Here we have to add 'club_formation' column from games!
    return club_games


def clean_clubs(clubs):
    clubs = clubs.drop(columns=['coach_name', 'total_market_value'])    # Both are null
    clubs['club_code'] = clubs['club_code'].astype('string')    # @Todo Choose if it is to maintain or not!
    clubs['name'] = clubs['name'].astype('string')
    clubs['domestic_competition_id'] = clubs['domestic_competition_id'].astype('string')    # Here as a Foreign Key!
    # @Todo resolve this:
    # There are players with 'current_club_id' set on clubs that have recorded 0 players in their squad!
    clubs['stadium_name'] = clubs['stadium_name'].astype('string')
    clubs.at[409, 'stadium_seats'] = 4851       # correcting the only 0 value!

    clubs['url'] = clubs['url'].astype('string')
    # @Todo still everything WIP here!
    return clubs
