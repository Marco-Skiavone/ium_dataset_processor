# The Result Log

> ## This is a file where we can add the gained knowledge about the dataset

---

# Appearance:

1. This is a set where players are into, in base of which game and how they have played.
2. **Note:**
   the **Appearance_id** is the combination of "*<game_id>*_*<player_id>*". $\rightarrow$ **This will need a type
   definition!**
3. We have many ***player_name*** that are **None** and that does not intersect with the ***player_id*** of the
**not-Null** rows, neither with the ids of the *players.csv* dataset $\rightarrow$ We have to decide if remove them or
not.
4. Remember to change the type of the ***player_name*** column into a *string*.
   (`app['player_name'] = app['player_name'].astype('string')`)
5. Finally, we must interpolate data and see where to put them.
6. There are **356** players_id rows (with duplicates) in appearance that are not in players csv
7. There are **42** `players_id` that are not in `players.csv`!

## Jsonifier
- `apprearance_id` is a String
- `player_name` is a String
- `competition_id` is a String
- `date` is a String
- `red_cards` is a Boolean
- dropped appearances with `player_id` not found in players dataset


---

# Clubs:

1. `coach_name` and `total_market_value` are both **NULL** columns $\rightarrow$ ***WE WILL REMOVE THEM!***
2. There are wrong sized clubs in the current clubs of players. **WHAT SHALL WE DO ?!**
3. There are players with `current_club_id` set on clubs that have recorded 0 players in their squad. **THIS IS A
   PROBLEM.**
4. `domestic_competition_id` is corresponding to `domestic_league_code` of **competitions** table.
5. We will rename:
   1. `name` into `club_name`
   2. `url` into `club_url`
   3. `domestic_competition_id` into `local_competition_code`.
   
> ###### 3. Should we update the clubs or remove both the records from the two tables ?
> ###### The wrong sized clubs COULD HAVE PROBABLY CEASED TO EXIST!
## We could remove `foreigners_percentage` and calculate it at runtime via server route.

---

# Club_games:

1. Every single field of this set is repeated twice. Furthermore, this set has the same data of **games**, but
   centralized on **clubs** view.

> ###### Surely, we could choose to maintain here many fields of _games_ and remove them from **games table**.
---

# Competitions:

1. `Confederation` column values are ever the same: "*europa*". This means that **probably** we can **remove** it.
2. We found out all the **international** competitions have matching ***Null*** values for the
   columns `country_id`, `country_name` and `domestic_league_code`. $\rightarrow$ Everything is still good with these
   values and the tuples are still valid!
3. We also found out that the columns `competition_code` and `name` have same values through all the csv.
4. The `domestic_competition_code` column has different values, but they are still used by more than one tuple. We need
   to check carefully where they are used in the dataset!
5. We should maintain `country_name` renamed as `country`, meanwhile `country_id` will be lost.
6. `domestic_competition_id` is equal to `domestic_league_code` in case of local competitions (e.g. *Italian Cup ==
   IT1*).
7. We will rename:
    1. `name` into `competition_name`
    2. `type` into `competition_type`
    3. `url` into `competition_url`

> ###### 2. What should we maintain between *country_id* and _country_name_?
> ###### 3. *'name'* has EVER the same value of 'competition_code'?
> ###### 4. Watch out the _domestic_competition_code_ column in other _.csv_ files!
> ###### 5. We cannot cast properly _domestic_competition_code_ to a boolean because some elements have different name, even if they are a domestic competition
> > ### End of analysis
---

# Game_events:

1. this sets represents events occurred during the game. That is way it has many references to other ids.
2. description has a hardly readable input. We **SHOULD** elaborate it.
3. In description, the number N followed by a dot is the Nth time someone does something in the following context.
4. It seems that only `substitutions` type has `not reported` and `NaN` value

> There are different types of events:
> - cards: type of card: ?(cause of card)
> - substitution: specified or not
> - shootout: (shootouts are like 1v1 for 5" and have been alternatives to the penalties(english for 'rigori'))
> - goals: 
>   how goal has been scored: number of the goal in the specified context, 
>   ?(how it has been done the assist, number of the assist by that player in the specified context)
> #### **Example:**
> ", Right-footed shot, 2. Tournament Goal Assist: , Pass, 1. Tournament Assist"

> ###### Cleaned version:
> 1. Removed all unnecessary `', '`
> 2. `description` column is string type, made of segment divided by commas, each of them gives further info about the
occurred event
> 3. All `'Not reported'` and `NaN` have been normalized to `None`
> > ### End of analysis
---

# Game_lineups:

1. The `number` column has few values set to _'-'_. We converted them to _None_ and set the column to float.
2. We have **consistency issues (around 14k tuples!)** with `player_id` and `player_name` columns!
3. All players position is properly set. We could decide to put this set in **MongoDB**.

> ###### 2. What should we do with that !?
> ## Probably the data will be fixed and elaborated via javascript by the client!
> > ### End of analysis
---

# Games:

1. `home_club_position` and `away_club_position` are relative to the **ranked list** of football clubs **AT THE MOMENT
   IN WHICH THE GAME STARTS!**
2. `aggregate` represents the final result of a game. Usually, given as *"<home_goals>:<away_goals>"*.
3. All the `aggregate` are consistent with data of goals.
4. We will rename:
    1. `date` into `game_date`
    2. `url` into `game_url`

---

# Players:

1. This is the set where are stored personal info about the players, many of which have a **static nature** (**SQL**).
2. Elements like the ***height_in_cm*** are of type **FLOAT** because of the *NaN* values. There is no decimal value,
   but we cannot cast the column to **INT** until we handle the missing values.
3. I set the **'position'** as a *category* type value, because I could and I thought it was right to do it.
4. The 'name' we find in the columns is the string concatenation of the ***'first_name'*** and the ***'last_name'*** . I
   found out the *'name'* is represented only by the *'last_name'*, when the *'first_name'* is missing.
5. We still have to deal with **many** columns that need ***Na*** handling.
6. `highest_market_value_in_eur` column may be renamed as `highest_val(K_eur)` and we can divide its values by **1000**.
7. `player_code` seems to be useless. But we could try to see if it can restore `first_name`. **Surely, we don't want to
   maintain its content in the servers!**
8. `contract_expiration_date` can be None or can (potentially) be a date in the past. So we must check it on
   Express/Spring-Boot to see if it is expired.
9. `current_club_name` and `current_club_domestic_competition_id` can be dropped because we see them from the club side.
10. `position` column has to be `None` when it has *value=='Missing'*. (There is a *@todo* commented code cell in
    *Players.ipynb*)
11. We will rename the following columns:
    1. `market_value_in_eur` to `value_eur`
    2. `highest_market_value_in_eur` to `top_value_eur`
12. We will rename:
    1. `name` into `player_name`
    2. `type` into `player_type`
    3. `url` into `player_url`

> ###### See *3.* of Clubs to resolve the issue about club_ids!
---

# Player_valuations:

1. `date` and `datetime` columns have the **same values**. $\rightarrow$ we removed the `datetime` columns.
2. `date` and `dateweek` columns have different values in **almost half of cases**, so they must be not the same thing.
3. We renamed the `player_club_domestic_competition_id` column in something shorter.
4. It seems that `n` column values are all ***1***. I can't figure out what it represents, so we could remove the
   column.
5. we will rename:
   1.`dateweek` into `date_week`
   2`player_club_domestic_competition_id` into `current_dom_competition_code`
   3`market_value_in_eur` into `market_value_eur`
    
> ### End of analysis
