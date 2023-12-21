import pandas as pd


def get_appearance(s):
    if s is None:
        return pd.read_csv('Assignment_Data_2023-2024/appearances.csv')
    else:
        return pd.read_csv(s + 'Assignment_Data_2023-2024/appearances.csv')


def get_club_games(s):
    if s is None:
        return pd.read_csv('Assignment_Data_2023-2024/club_games.csv')
    else:
        return pd.read_csv(s + 'Assignment_Data_2023-2024/club_games.csv')


def get_clubs(s):
    if s is None:
        return pd.read_csv('Assignment_Data_2023-2024/clubs.csv')
    else:
        return pd.read_csv(s + 'Assignment_Data_2023-2024/clubs.csv')


def get_competitions(s):
    if s is None:
        return pd.read_csv('Assignment_Data_2023-2024/competitions.csv')
    else:
        return pd.read_csv(s + 'Assignment_Data_2023-2024/competitions.csv')


def get_game_events(s):
    if s is None:
        return pd.read_csv('Assignment_Data_2023-2024/game_events.csv')
    else:
        return pd.read_csv(s + 'Assignment_Data_2023-2024/game_events.csv')


def get_game_lineups(s):
    if s is None:
        return pd.read_csv('Assignment_Data_2023-2024/game_lineups.csv')
    else:
        return pd.read_csv(s + 'Assignment_Data_2023-2024/game_lineups.csv')


def get_games(s):
    if s is None:
        return pd.read_csv('Assignment_Data_2023-2024/games.csv')
    else:
        return pd.read_csv(s + 'Assignment_Data_2023-2024/games.csv')


def get_player_valuations(s):
    if s is None:
        return pd.read_csv('Assignment_Data_2023-2024/player_valuations.csv')
    else:
        return pd.read_csv(s + 'Assignment_Data_2023-2024/player_valuations.csv')


def get_players(s):
    if s is None:
        return pd.read_csv('Assignment_Data_2023-2024/players.csv')
    else:
        return pd.read_csv(s + 'Assignment_Data_2023-2024/players.csv')
