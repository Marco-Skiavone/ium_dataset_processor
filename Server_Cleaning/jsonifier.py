from Server_Cleaning.modules.module_for_imports import *


def json_wrapper(loc=''):
    dfs = clean_club_games(get_club_games(loc), loc)
    dfs[0].to_json('Cleaned_Json/cleaned_club_games.json', orient='records', indent=2)
    dfs[0] = None
    print('.', end='')

    dfs[1].to_json('Cleaned_Json/cleaned_games.json', orient='records', indent=2)
    print('.', end='')

    app = clean_appearances(get_appearances(), dfs[1], loc)
    app.to_json('Cleaned_Json/cleaned_appearances.json', orient='records', indent=2, date_format='%d-%m-%Y')
    app = None
    print('.', end='')

    game_lineups = clean_game_lineups(get_game_lineups(), dfs[1])
    game_lineups.to_json('Cleaned_Json/cleaned_game_lineups.json', orient='records', indent=2)
    game_lineups = None
    print('.', end='')

    game_events = clean_game_events(get_game_events(loc), dfs[1], loc)
    dfs[1] = None
    dfs = None
    game_events.to_json('Cleaned_Json/cleaned_game_events.json', orient='records', indent=2)
    print('.', end='')
    game_events = None
    return


# Processing the dataset
print('Starting: [', end='')

location = '../'

clubs = clean_clubs(get_clubs(location))
clubs.to_json('Cleaned_Json/cleaned_clubs.json', orient='records', indent=2)
clubs = None
print('.', end='')

json_wrapper(location)

competitions = clean_competitions(get_competitions(location))
competitions.to_json('Cleaned_Json/cleaned_competitions.json', orient='records', indent=2)
competitions = None
print('.', end='')

player_valuations = clean_player_valuations(get_player_valuations(location))
player_valuations.to_json('Cleaned_Json/cleaned_player_valuations.json', orient='records', indent=2,
                          date_format='%d-%m-%Y')
player_valuations = None
print('.', end='')

players = clean_players(get_players(location))
players.to_json('Cleaned_Json/cleaned_players.json', orient='records', indent=2, date_format='%d-%m-%Y')
players = None
print('.', end='')

flags = create_flags(location)
flags.to_json('Cleaned_Json/cleaned_flags.json', orient='records', indent=2)
flags = None
print('.] Done.')
