# Definition of "clear_" functions for the queries
from Assignment_Queries.pandas_lib.std_imports import *
from Server_Cleaning.modules.Assignment_datasets import *


def clear_clubs(clubs):
    if clubs is None:
        print('Error in clear_clubs()')
    else:
        clubs = clubs.drop(columns=['url', 'coach_name', 'club_code', 'total_market_value', 'stadium_name'])
        clubs['net_transfer_record'] = clubs['net_transfer_record'].astype('string')
        clubs['net_transfer_record'] = (clubs['net_transfer_record'].apply(clean_net_records)).astype('int')
        clubs['name'] = clubs['name'].str.replace('Football Club', "FC", regex=False)
        clubs['name'] = clubs['name'].str.replace('"', "'", regex=False)
        clubs['domestic_competition_id'] = clubs['domestic_competition_id'].astype('string')
        clubs.fillna({'foreigners_percentage': 0}, inplace=True)
        clubs['foreigners_percentage'] = clubs['foreigners_percentage'].astype('int')
    return clubs


def clear_club_games(cg):
    if cg is None:
        print('Error in clear_club_games()')
    else:
        cg = cg.drop(columns=['opponent_manager_name', 'own_manager_name'])
        # Data cleaning for this task: Still WIP!
        # cg.loc[cg['own_position'].isnull(), 'own_position'] = -1
        # cg.loc[cg['opponent_position'].isnull(), 'opponent_position'] = -1
        cg['own_position'] = cg['own_position'].astype('float')
        cg['opponent_position'] = cg['opponent_position'].astype('float')
        cg['hosting'] = (cg['hosting'].apply(lambda x: bool(x.__str__() == 'Home'))).astype('bool')
        cg['is_win'] = (cg['is_win'].apply(lambda x: bool(x == 1))).astype('bool')
        # setting 2 lines from 1:
        # games_subset_1 = games[['game_id', 'home_club_id', 'home_club_formation']].copy()
        # games_subset_2 = games[['game_id', 'away_club_id', 'away_club_formation']].copy()
        # games_subset_1 = games_subset_1.rename(columns={'home_club_id': 'club_id',
        #                                                 'home_club_formation': 'club_formation'})
        # games_subset_2 = games_subset_2.rename(columns={'away_club_id': 'club_id',
        #                                                 'away_club_formation': 'club_formation'})
        # game_subset = pd.concat([games_subset_1, games_subset_2], axis=0)
        # games_subset_1 = None
        # games_subset_2 = None
        # cg = pd.merge(cg, game_subset, on=['game_id', 'club_id'])
        # cg['club_formation'] = cg['club_formation'].astype('string')
        # games_subset = None
    return cg


def clear_games(ga):
    if ga is None:
        print('Error in clear_games()')
    else:
        ga = ga.drop(columns=['home_club_manager_name', 'away_club_manager_name', 'round', 'stadium',
                              'referee', 'home_club_name', 'away_club_name', 'competition_type', 'url'])
        ga = ga.replace(float('NaN'), None)
        ga['competition_id'] = ga['competition_id'].astype('string')
        ga['date'] = pd.to_datetime(ga['date'].astype('string'))
        ga['home_club_formation'] = ga['home_club_formation'].astype('string')
        ga['away_club_formation'] = ga['away_club_formation'].astype('string')
        ga['aggregate'] = ga['aggregate'].astype('string')
        # Data cleaning for this task: Still WIP!
        # ga.loc[ga['attendance'].isna(), 'attendance'] = -1
        # ga.loc[ga['home_club_position'].isna(), 'home_club_position'] = -1
        # ga.loc[ga['away_club_position'].isna(), 'away_club_position'] = -1
        ga['attendance'] = ga['attendance'].astype('float')
        ga['home_club_position'] = ga['home_club_position'].astype('float')
        ga['away_club_position'] = ga['away_club_position'].astype('float')
    return ga


def clear_game_events(g_ev):
    if g_ev is None:
        print('Error in clear_game_events()')
    else:
        g_ev.fillna({'player_in_id': -1, 'player_assist_id': -1}, inplace=True)
        g_ev['player_in_id'] = g_ev['player_in_id'].astype('int')
        g_ev['player_assist_id'] = g_ev['player_assist_id'].astype('int')
        g_ev['game_event_id'] = g_ev['game_event_id'].astype('string')
        g_ev['type'] = g_ev['type'].astype('string')
        g_ev['description'] = g_ev['description'].astype('string')
    return g_ev


def check_home_win(x):
    """ Used in apply to return a column with string values passing 'aggregate' format to it
        :param x: A value of 'aggregate' column in the 'x:y' format where x, y are numbers
    """
    i = x.find(':')
    first = int(x[:i])
    second = int(x[i + 1:])
    return 'win' if first > second else 'loss' if second > first else 'draw'
