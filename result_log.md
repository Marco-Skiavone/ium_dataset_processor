# The Result Log
> ## This is a file where we can add the gained knowledge about the dataset

---
# Appearance:
1. This is a set where players are into, in base of which game and how they have played.
2. **Note:**
the **Appearance_id** is the combination of "*<game_id>*_*<player_id>*". $\rightarrow$ **This will need a type definition!** 
3. We have many ***player_name*** that are **None** and that does not intersect with the ***player_id*** of the **not-Null** rows, neither with the ids of the *players.csv* dataset $\rightarrow$ We have to decide if remove them or not.
4. Remember to change the type of the ***player_name*** column into a *string*. 
(`app['player_name'] = app['player_name'].astype('string')`)
5. Finally, we must interpolate data and see where to put them.
---
# Players:
1. This is the set where are stored personal info about the players, many of which have a **static nature** (**SQL**).
2. Elements like the ***height_in_cm*** are of type **FLOAT** because of the *NaN* values. There is no decimal value, but we cannot cast the column to **INT** until we handle the missing values.
3. I set the **'position'** as a *category* type value, because I could and I thought it was right to do it.
4. The 'name' we find in the columns is the string concatenation of the ***'first_name'*** and the ***'last_name'*** . I found out the *'name'* is represented only by the *'last_name'*, when the *'first_name'* is missing.
5. We still have to deal with **many** columns that need ***Na*** handling.
6. '`highest_market_value_in_eur`' column may be renamed as '`highest_val(K_eur)`' and we can divide its values by **1000**. 
7. **...**
---