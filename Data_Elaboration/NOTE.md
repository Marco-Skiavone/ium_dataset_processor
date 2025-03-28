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
    - ```player_id``` $\rightarrow$ like ```game_id``` it's present as a foreign key of Players set

---

# Clubs:

1. This set represents a football team
2. If I were to transpose this dataset into SQL I would do so by retaining the following attributes to the relevant
   entity:
    - **club_id** (identifier)
    - ```name``` $\rightarrow$ it is the name of the club
    - ```foreigners_percentage``` $\rightarrow$ it is the percentage of foreign player in the club
    - ```squad_size``` $\rightarrow$ it is the number of player in the club
    - ```foreigners_number``` $\rightarrow$ it is the number of foreign players in the club
    - ```url``` $\rightarrow$ it is the url to the page of the club
    - ```net_transfer_record``` $\rightarrow$ it indicates the net transfer record for a transaction
    - ```national_team_players``` $\rightarrow$ it indicates the number of player from the same nation of the club
    - ```stadium_seats``` $\rightarrow$ it indicates the number of stadium seats
    - ```last_season``` $\rightarrow$ it indicates the year of the last season played by the team
    - ```stadium_name``` $\rightarrow$ it is the name of the home stadium of the club
    - ```average_age``` $\rightarrow$ it is the average age of the player of the team
    - ```club_code``` **(not sure to maintain)** $\rightarrow$ it is an alternative identification code for the club

3. Instead, I would discard or arrange differently the sequent information in the csv:
    - ```domestic_competition_id``` $\rightarrow$ it will be present as a reference to the competition
    - ```coach_name``` and ```total_market_value``` $\rightarrow$ both are null, so we discarded them

---

# Players:

1. This set represents a football player
2. If I were to transpose this dataset into SQL I would do so by retaining the following attributes to the relevant
   entity:
    - **player_id** (identifier)
    - ```name``` $\rightarrow$ it is the full name of the player
    - ```current_club_id``` $\rightarrow$ it indicates the current club that the player plays for
    - ```sub_position``` $\rightarrow$ it indicates an alternative position that the player plays in
    - ```country_of_birth``` $\rightarrow$ it is the country where the player was born
    - ```country_of_citizenship``` $\rightarrow$ it is the country where the player lives
    - ```height_in_cm``` $\rightarrow$ it is the height of the player
    - ```market_value_in_eur``` $\rightarrow$ it is the value of the player if another club wants to buy it
    - ```url``` $\rightarrow$ it is the url to the player's page
    - ```highest_market_value_in_eur``` $\rightarrow$ it is the highest record of the market value of a player
    - ```position``` $\rightarrow$ it indicates the main position that the player plays in
    - ```image_url``` $\rightarrow$ it is a link to a picture of the player
    - ```foot``` $\rightarrow$ it indicates which foot the player tends to shoot with
    - ```date_of_birth``` $\rightarrow$ it indicates when the player was born
    - ```city_of_birth``` $\rightarrow$ it indicates the city where the player was born
    - ```agent_name``` $\rightarrow$ it is the full name of the player's agent
    - ```contract_expiration_date``` $\rightarrow$ it indicates when the contract with a club will expire
    - ```last_season``` $\rightarrow$ it indicates the year of the last season played by the player
3. Instead, I would discard or arrange differently the sequent information in the csv:
    - ```firs_name``` and ```last_name``` $\rightarrow$ this information are preset in name
    - ```player_code``` $\rightarrow$ this information is unuseful, the set already has an identifier
    - ```current_club_name``` $\rightarrow$ this information is unuseful, its sufficient ```current_club_id```
    - - ```current_club_domestic_competition_id``` $\rightarrow$ it indicates the competition
         in which the player's team is participating

---

# Appearance:

1. This set represents every appearance of a player in a past match and some information related to that appearance
2. If I were to transpose this dataset into SQL I would do so by retaining the following attributes to the relevant
   entity:
    - **appearance_id** (identifier)
    - ```minutes_played``` $\rightarrow$ it indicates how many minutes a player played in a certain game
    - ```yellow_cards``` $\rightarrow$ it indicates the number of yellow card that a player get during a certain game
    - ```player_current_club_id``` $\rightarrow$ it is a redundant data, it is the same data of current_club_id in the
      player table
    - ```player_club_id``` $\rightarrow$ it indicates in which club the player was playing when it appeared
    - ```assists``` $\rightarrow$ it indicates the number of assists of the player during a certain game
    - ```red_cards``` $\rightarrow$ it indicates the number of red cards that a player get during a certain game
    - ```goals``` $\rightarrow$ it is the number of goals scored by a player during a certain game
3. Instead, I would discard or arrange differently the sequent information in the csv:
    - ```game_id``` $\rightarrow$ It will be present as a foreign key
    - ```player_id``` $\rightarrow$ It will be present as a foreign key
    - ```date``` $\rightarrow$ it's an information relative to the game and it is redundant
    - ```player_name``` $\rightarrow$ it's an information relative to the player and it's redundant
    - ```competition_id``` $\rightarrow$ it's an information relative to the game and it's redundant

---

# Competition:

1. This set represents the various championships, and it's a bit odd
2. If I were to transpose this dataset into SQL I would do so by retaining the following attributes to the relevant
   entity:
    - **competition_id** (identifier)
    - ```name``` $\rightarrow$ it is the name of the competition
    - ```competition_code``` $\rightarrow$ it is another identification code of the competition
    - ```type``` $\rightarrow$ it is the kind of competition
    - ```sub_type``` $\rightarrow$ it indicates more precisely the kind of competition
    - ```country_name``` $\rightarrow$ it indicates the nation of the competition if it takes place in only one nation
    - ```domestic_league_code``` $\rightarrow$ in case it is a national competition it indicates the code of the
      domestic league
    - ```url``` $\rightarrow$ it is a link to the competition's web page
3. Instead, I would discard or arrange differently the sequent information in the csv:
    - ```confederation``` $\rightarrow$ It has the only value 'europa'
    - ```country_id``` $\rightarrow$ contains irrelevant data
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
    - ```own_goals``` $\rightarrow$ it is the number of goals of a club in a certain game
    - ```own_position``` $\rightarrow$ it is the team's ranking position after a certain game
    - ```own_manager_name``` $\rightarrow$ it is the name of the manager of the club during a certain game
    - ```hosting``` $\rightarrow$ it indicates if the club is hosting or not the game
    - ```is_win``` $\rightarrow$ it indicates if the club is winning the game or not
    - ```club_formation``` (not sure) $\rightarrow$ it is an information derived from the games table, it indicates the
      formation of the club for a certain game
5. The attributes ```opponent_id```, ```opponent_goals```, ```opponent_position``` and ```opponent_manager_name``` will
   be passed to their counterparts while maintaining the same ```game_id```
6. To be safe, I would check if by default the ```games_id``` is repeated twice within this set

---

# Player_valuation:

1. This set represents various player-related information that varies over time. The particular structure of this set
   makes it a perfect candidate for inclusion in **mongoDB**.
2. Nonetheless, some data needs to be revised or is not consistent, for example:
    - we need to determine the differences between ```date```, ```datetime``` and ```dateweek```, probably they describe
      the same data, and we can maintain only one of them
    - the attribute ```n``` has always the value set to 1
3. The attributes at the end of the process will be these:
    - ```player_id``` $\rightarrow$ it is the identification code of the player
    - ```last_season``` $\rightarrow$ it is the year of the last season played by the player at the time of the
      valuation
    - ```date``` $\rightarrow$ it is the date of the valuation
    - ```market_value_in_eur``` $\rightarrow$ it is the value of the player at the time of the valuation
    - ```current_club_id``` $\rightarrow$ it is the player's current club at the time of the valuation
    - ```player_club_domestic_competition_id``` $\rightarrow$ it is the competition the player's team was participating
      in at the time

---

# Game_lineups:

1. This set represents various information about a player of a certain club during a certain game.
2. I think this is a valid set to insert into mongoDB, because those data aren't requested from any other entity
3. At the same time some attributes could be foreign key if I create game_lineups as a SQL entity, those attributes are:
    - ```game_id```
    - ```club_id```
    - ```player_id```
4. The attributes at the end of the process will be these:
   - ```game_lineups_id``` $\rightarrow$ it is the identification code of the lineup
   - ```type``` $\rightarrow$ it is the type of lineup, it could change during a match
   - ```number``` $\rightarrow$ it is the number of tshirt of the player
   - ```team_captain``` $\rightarrow$ it indicates if the player is the captain of the team
   - ```position``` $\rightarrow$ it indicates the position of the player on the soccer field
   - ```player_name``` (not sure to maintain) $\rightarrow$ it is the player full name