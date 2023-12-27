# Matteo's notes

> ## In this file you can find the directions found by Matteo during his data analysis, it might help you in the data analysis phase

---

# Games:

1. In this data set is information on matches that have already occurred
2. If I were to transpose this dataset into SQL I would do so by retaining the following attributes to the relevant
   entity:
    - **game_id** (identifier)
    - ```aggregate``` $\rightarrow$ it is the aggregate score of a match relating to both teams
    - ```referee``` $\rightarrow$ it is the arbiter of the match
    - ```stadium``` $\rightarrow$ it is where is set the match
    - ```round``` $\rightarrow$ it is the round of the game
    - ```season``` $\rightarrow$ it is the season year
    - ```date``` $\rightarrow$ it is when is set the game
    - ```attendance``` $\rightarrow$ it is the number of audience
    - ```url```
3. Instead, I would discard or arrange differently the sequent information in the csv:
    - ```competition_id``` $\rightarrow$ is information about the Competition entity and will later be bound via a
      foreign key to the Games
    - ```home_club_id``` and ```away_club_id``` $\rightarrow$ are the identifiers of the two playing teams, I decided
      not to keep them to
      maintain better data consistency
    - ```home_club_goals``` and ```away_club_goals``` $\rightarrow$ are the numbers of goals scored by the respective
      teams, I decided to
      condense them into a single attribute in the Club_games relationship
    - ```home_club_position``` and ```away_club_position``` $\rightarrow$ are the positions in the championship ranking
      relating to a team, I
      also decided to condense this into a single attribute in the Club_games relation
    - ```home_club_manager_name``` and ```away_club_manager_name``` $\rightarrow$ I'm still not completely sure what
      they are, but I think they
      are the names of the coaches of the two teams for that specific match, also in this case I decided to insert them
      together in Club_games
    - ```home_club_formation``` and ```away_club_formation``` $\rightarrow$ are the formations of the two teams
      maintained during the match, like
      the other cases I have condensed them in Club_games
    - ```home_club_name``` and ```away_club_name``` $\rightarrow$ I decided not to keep them as they are data already
      present in Club and would
      therefore be redundant
    - ```competition_type``` $\rightarrow$ this data is related to competition, so as in competition_id I decided not to
      reinsert it to
      avoid redundancy

---

# Game_events:

1. This set represents an event, such as assist or player change, which affects one or more players of a certain team
   during a certain match
2. If I were to transpose this dataset into SQL I would do so by retaining the following attributes to the relevant
   entity:
    - **game_event_id** (identifier)
    - ```type``` $\rightarrow$ it indicate the kind of game event
    - ```description``` $\rightarrow$ it is a short description of the game event
    - ```player_assist_id``` $\rightarrow$ in case the event is an assist it indicates the player that did the assist
    - ```club_id``` $\rightarrow$ it indicates the club of the player when it did the event, it's a redundant data, but
      it's a nice to have
    - ```player_in_id``` $\rightarrow$ in case the event is a substitution it indicates the player that substitute the
      main player
    - ```minute``` $\rightarrow$ it indicates the minute of the game when the event occur
3. Instead, I would discard or arrange differently the sequent information in the csv:
    - ```date``` $\rightarrow$ it's the date of the match and I decided to discard it because it's already present in
      the Games set
    - ```game_id``` $\rightarrow$ actually it's present as a foreign key of Games set
    - ```player_id``` $\rightarrow$ like game_id it's present as a foreign key of Players set

---

# Clubs:

1. This set represents a football team
2. If I were to transpose this dataset into SQL I would do so by retaining the following attributes to the relevant
   entity:
    - **club_id** (identifier)
    - name
    - foreigners_percentage: It's calculated as
    - squad_size
    - foreigners_number
    - url
    - net_transfer_record
    - national_team_players
    - stadium_seats
    - last_season
    - stadium_name
    - average_age
    - club_code (not sure to maintain)

3. Instead, I would discard or arrange differently the sequent information in the csv:
    - domestic_competition_id: it will be present as a reference to the competition
    - coach_name and total_market_value: both are null, so we discarded them

---

# Players:

1. This set represents a football player
2. If I were to transpose this dataset into SQL I would do so by retaining the following attributes to the relevant
   entity:
    - **player_id** (identifier)
    - name
    - current_club_id
    - sub_position
    - country_of_birth
    - country_of_citizenship
    - height_in_cm
    - current_club_name
    - market_value_in_eur
    - url
    - highest_market_value_in_eur
    - position
    - image_url
    - foot
    - current_club_domestic_competition_id
    - date_of_birth
    - city_of_birth
    - agent_name
    - player_code (not sure to maintain)
    - contract_expiration_date
    - last_season
3. Instead, I would discard or arrange differently the sequent information in the csv:
    - firs_name and last_name: this information are preset in name
    - player_code: this information is unuseful, the set already has an identifier
    - current_club_name: this information is unuseful, its sufficient current_club_id

---

# Appearance:

1. This set represents every appearance of a player in a past match and some information related to that appearance
2. If I were to transpose this dataset into SQL I would do so by retaining the following attributes to the relevant
   entity:
    - **appearance_id** (identifier)
    - minutes_played
    - yellow_cards
    - player_current_club_id
    - player_club_id
    - assists
    - red_cards
    - goals
3. Instead, I would discard or arrange differently the sequent information in the csv:
    - game_id: It will be present as a foreign key
    - player_id: It will be present as a foreign key
    - date: it's an information relative to the game and it is redundant
    - player_name: it's an information relative to the player and it's redundant
    - competition_id: it's an information relative to the game and it's redundant

---

# Competition:

1. This set represents the various championships, and it's a bit odd
2. If I were to transpose this dataset into SQL I would do so by retaining the following attributes to the relevant
   entity:
    - **competition_id** (identifier)
    - name
    - competition_code
    - type
    - sub_type
    - country_name
    - domestic_league_code
    - url
3. Instead, I would discard or arrange differently the sequent information in the csv:
    - confederation: It has the only value 'Europa'
    - country_id: contains irrelevant data
4. We could put this set in **mongoDB**

---

# Club_games:

1. This data set represents information related to a specific game, such as scores and lineups.
2. This dataset is special, as I represent it as a relationship, so its identifiers are actually foreign keys to Clubs
   and Games.
3. Furthermore, for ease of representation, I made sure that each tuple only takes into consideration the information of
   one team at a time. According to this logic, therefore, each match will appear in this set twice, in order to
   represent the data of both playing teams
4. The attributes at the end of the process will be these:
    - **game_id** and **club_id** as identifiers
    - own_goals
    - own_position
    - own_manager_name
    - hosting
    - is_win
    - club_formation (not sure)
5. The attributes opponent_id, opponent_goals, opponent_position and opponent_manager_name will be passed to their
   counterparts while maintaining the same game_id
6. To be safe, I would check if by default the games_id is repeated twice within this set

---

# Player_valuation:

1. This set represents various player-related information that varies over time. The particular structure of this set
   makes it a perfect candidate for inclusion in **mongoDB**.
2. Nonetheless, some data needs to be revised or is not consistent, for example:
    - we need to determine the differences between date, datetime and dateweek, probably they describe the same data,
      and we can maintain only one of them
    - the attribute n has always the value set to 1

---

# Game_lineups:

1. This set represents various information about a player of a certain club during a certain game.
2. I think this is a valid set to insert into mongoDB, because those data aren't requested from any other entity
3. At the same time some attributes could be foreign key if I create game_lineups as a SQL entity, those attributes are:
    - game_id
    - club_id
    - player_id
   
