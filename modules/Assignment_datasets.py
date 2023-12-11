import pandas as pd


def get_appearance():
    return pd.read_csv('Assignment_Data_2023-2024/appearances.csv')


def get_club_games():
    return pd.read_csv('Assignment_Data_2023-2024/club_games.csv')


def get_clubs():
    return pd.read_csv('Assignment_Data_2023-2024/clubs.csv')


def get_competitions():
    return pd.read_csv('Assignment_Data_2023-2024/competitions.csv')


def get_game_events():
    return pd.read_csv('Assignment_Data_2023-2024/game_events.csv')


def get_game_lineups():
    return pd.read_csv('Assignment_Data_2023-2024/game_lineups.csv')


def get_games():
    return pd.read_csv('Assignment_Data_2023-2024/games.csv')


def get_player_valuations():
    return pd.read_csv('Assignment_Data_2023-2024/player_valuations.csv')


def get_players():
    return pd.read_csv('Assignment_Data_2023-2024/players.csv')
