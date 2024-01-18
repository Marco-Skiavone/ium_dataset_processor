from modules.module_for_imports import *

# Processing the dataset

app = clean_appearances(get_appearances())
app.to_json('Cleaned_Json/cleaned_appearances.json', orient='records', indent=2)
app = None

club_games = clean_club_games(get_club_games())
club_games.to_json('Cleaned_Json/cleaned_club_games.json', orient='records', indent=2)
club_games = None

clubs = clean_clubs(get_clubs())
clubs.to_json('Cleaned_Json/cleaned_clubs.json', orient='records', indent=2)
clubs = None

competitions = clean_competitions(get_competitions())
competitions.to_json('Cleaned_Json/cleaned_competitions.json', orient='records', indent=2)
competitions = None

game_events = clean_game_events(get_game_events())
game_events.to_json('Cleaned_Json/cleaned_game_events.json', orient='records', indent=2)
game_events = None

game_lineups = clean_game_lineups(get_game_lineups())
game_lineups.to_json('Cleaned_Json/cleaned_game_lineups.json', orient='records', indent=2)
game_lineups = None

games = clean_games(get_games())
games.to_json('Cleaned_Json/cleaned_games.json', orient='records', indent=2)
games = None

player_valuations = clean_player_valuations(get_player_valuations())
player_valuations.to_json('Cleaned_Json/cleaned_player_valuations.json', orient='records', indent=2)
player_valuations = None

players = clean_players(get_players())
players.to_json('Cleaned_Json/cleaned_players.json', orient='records', indent=2)
players = None

print('Done.')
