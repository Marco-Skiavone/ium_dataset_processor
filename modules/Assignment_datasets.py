import pandas as pd


def get_appearance(s=''):
    return pd.read_csv(s + 'Assignment_Data_2023-2024/appearances.csv')


def get_club_games(s=''):
    return pd.read_csv(s + 'Assignment_Data_2023-2024/club_games.csv')


def get_clubs(s=''):
    return pd.read_csv(s + 'Assignment_Data_2023-2024/clubs.csv')


def get_competitions(s=''):
    return pd.read_csv(s + 'Assignment_Data_2023-2024/competitions.csv')


def get_game_events(s=''):
    return pd.read_csv(s + 'Assignment_Data_2023-2024/game_events.csv')


def get_game_lineups(s=''):
    return pd.read_csv(s + 'Assignment_Data_2023-2024/game_lineups.csv')


def get_games(s=''):
    return pd.read_csv(s + 'Assignment_Data_2023-2024/games.csv')


def get_player_valuations(s=''):
    return pd.read_csv(s + 'Assignment_Data_2023-2024/player_valuations.csv')


def get_players(s=''):
    return pd.read_csv(s + 'Assignment_Data_2023-2024/players.csv')
