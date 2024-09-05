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
        cg['own_position'] = cg['own_position'].astype('float')
        cg['opponent_position'] = cg['opponent_position'].astype('float')
        cg['hosting'] = (cg['hosting'].apply(lambda x: bool(x.__str__() == 'Home'))).astype('bool')
        cg['is_win'] = (cg['is_win'].apply(lambda x: bool(x == 1))).astype('bool')
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


def clear_player_valuations(pl_val, comps):
    if pl_val is None:
        print('Error in clear_player_valuations()')
    else:
        # Renaming columns
        pl_val = pl_val.rename(columns={'player_club_domestic_competition_id': 'local_competition_code',
                                        'market_value_in_eur': 'market_value_eur'})
        pl_val = pl_val.drop(columns=['dateweek', 'datetime', 'n'])
        # Type parsing
        pl_val['last_season'] = pl_val['last_season'].astype('int')
        pl_val = pl_val[pl_val['last_season'] > 2021]
        pl_val['date'] = pd.to_datetime(pl_val['date'].astype('string'))
        pl_val = pl_val.sort_values(by='date', ignore_index=True, ascending=False)
        pl_val['local_competition_code'] = (
            pl_val['local_competition_code'].astype('string'))
        pl_val = pl_val.drop_duplicates('player_id')
        pl_val = pl_val[['player_id', 'market_value_eur', 'local_competition_code']]
        # Setting the code to the corresponding country
        comps = comps[
            ['country_name', 'domestic_league_code']].dropna().drop_duplicates().reset_index()
        comps = comps.rename(columns={'domestic_league_code': 'local_competition_code'})
        pl_val = pl_val.merge(comps, on='local_competition_code', how='inner')[
            ['player_id', 'country_name', 'market_value_eur']]
    return pl_val


def check_home_win(x):
    """ Used in apply to return a column with string values passing 'aggregate' format to it
        :param x: A value of 'aggregate' column in the 'x:y' format where x, y are numbers
    """
    i = x.find(':')
    first = int(x[:i])
    second = int(x[i + 1:])
    return 'win' if first > second else 'loss' if second > first else 'draw'


def card_converter(x):
    """
    Used in apply to modify the card column to cleaning the text inside
    """
    if 'red' in x or 'Red' in x:
        return 'red'
    elif 'yellow' in x or 'Yellow' in x:
        return 'yellow'
    else:
        return 'goal'


def fill_age(x):
    """
    Used in apply to modify a partial game event column to substituting the date_of_birth of a player with his age
    """
    date0 = x['date']
    if '-' in date0:
        year0 = int(date0[:date0.find('-')])

        date1 = x['date_of_birth']
        if '-' in date1:
            year1 = (int(date1[:date1.find('-')]))
            x['date_of_birth'] = year0 - year1

    return x


def generate_top_payed_players(path) :
    """
        used to retrieve the correct dataset for player_analysis.ipynb
    """
    game_events_csv = get_game_events(path)
    player_val_clean = clean_player_valuations(get_player_valuations(path))
    players_clean = clean_players(get_players(path))

    # skimming useless columns and old data
    players_names = players_clean.drop(columns=['last_name', 'last_season',
                                                'current_club_id', 'country_of_birth', 'city_of_birth',
                                                'country_of_citizenship', 'date_of_birth', 'sub_position', 'position',
                                                'foot', 'height_in_cm', 'value_eur', 'top_value_eur',
                                                'contract_expiration_date', 'agent_name', 'image_url'])

    player_val_2022 = player_val_clean.drop(columns=['date', 'date_week',
                                                     'current_club_id', 'current_dom_competition_code'])[
        player_val_clean['last_season'] > 2021]
    player_val_2022 = player_val_2022.loc[player_val_2022['player_id'].isin(players_names['player_id'])]
    top_payed_players = player_val_2022.drop_duplicates('player_id', keep='last').sort_values(by='market_value_eur',
                                                                                              ascending=False).head(100)

    # filtering consistent players
    top_payed_players_names = players_names.query('player_id.isin(@top_payed_players.player_id)', engine='python')

    # cleaning game events, keeping top valued players
    game_events = game_events_csv[game_events_csv['type'] != "Shootout"].copy()
    game_events['date'] = game_events['date'].astype('datetime64[ns]')
    game_events = game_events[game_events['date'] > pd.to_datetime("2021-12-31")]
    top_payed_game_events = game_events[game_events['player_id'].isin(top_payed_players_names['player_id'])].drop(
        columns=['game_id', 'game_event_id', 'date', 'type', 'club_id', 'player_in_id', 'player_assist_id']).dropna()

    # replacing player id with actual players names
    top_payed_game_events = pd.merge(top_payed_game_events, players_names, on='player_id', how='left').drop(
        columns=['player_id'])

    # creating minute range!!!
    bins = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90,
            120]  # 90 is for the goals occurred after the 90th minute
    bins_by_ten = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 120]
    top_payed_game_events.loc[:, 'minute_range'] = pd.cut(top_payed_game_events['minute'], bins=bins_by_ten)
    top_payed_game_events = top_payed_game_events.drop(columns=['minute'])

    # applying function above
    top_payed_game_events['description'] = top_payed_game_events['description'].apply(
        lambda x: event_description_modifier(x))

    return top_payed_game_events


# description cleaning
def event_description_modifier(x):
    """
    Used in apply to modify the description column to cleaning the text inside
    """
    if 'red' in x or 'Red' in x:
        return 'Red Card'
    elif 'yellow' in x or 'Yellow' in x:
        return 'Yellow Card'
    elif 'goal' in x or 'Goal' in x:
        return 'Goal'
    else:
        return 'Substitution'


