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
    clubs.rename(columns={'name': 'club_name', 'domestic_competition_id': 'local_competition_code', 'url': 'club_url'})
    # @Todo resolve this:
    # - There are players with 'current_club_id' set on clubs that have recorded 0 players in their squad!
    players = get_players()
    clubs['squad_size'] = clubs.apply(lambda x: search_squad_players(x, players))
    players = None

    clubs['stadium_name'] = clubs['stadium_name'].astype('string')
    clubs.at[409, 'stadium_seats'] = 4851       # correcting the only 0 value!

    clubs['url'] = clubs['url'].astype('string')
    # @Todo still everything WIP here!
    return clubs


def search_squad_players(x, players):
    if x['squad_size'] == 0:
        x['squad_size'] = players.query('current_club_id == @x.club_id').shape[0]
    return x
