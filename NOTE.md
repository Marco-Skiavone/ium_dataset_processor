# Matteo's notes
> ## In this file you can find the directions found by Matteo during his data analysis, it might help you in the data analysis phase

---
# Games:
1. In this data set is information on matches that have already occurred
2. If I were to transpose this dataset into SQL I would do so by retaining the following attributes to the relevant entity:
    - **game_id** (identifier)
    - aggregate
    - referee
    - stadium
    - round
    - season
    - date
    - attendance
    - url
3. Instead, I would discard or arrange differently the sequent information in the csv:
    - competition_id: is information about the Competition entity and will later be bound via a foreign key to the Games
    - home_club_id and away_club_id: are the identifiers of the two playing teams, I decided not to keep them to maintain better data consistency
    - home_club_goals and away_club_goals: are the numbers of goals scored by the respective teams, I decided to condense them into a single attribute in the Club_games relationship
    - home_club_position and away_club_position: are the positions in the championship ranking relating to a team, I also decided to condense this into a single attribute in the Club_games relation
    - home_club_manager_name and away_club_manager_name: I'm still not completely sure what they are, but I think they are the names of the coaches of the two teams for that specific match, also in this case I decided to insert them together in Club_games
    - home_club_formation and away_club_formation: are the formations of the two teams maintained during the match, like the other cases I have condensed them in Club_games
    - home_club_name and away_club_name: I decided not to keep them as they are data already present in Club and would therefore be redundant
    - competition_type: this data is related to competition, so as in competition_id I decided not to reinsert it to avoid redundancy