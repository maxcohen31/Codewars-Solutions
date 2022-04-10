/* Your Query Here */
SELECT yankees.player_name, yankees.games, CAST(ROUND(yankees.hits / yankees.at_bats::decimal, 3) AS VARCHAR(6)) AS batting_average
FROM yankees
WHERE yankees.at_bats >= 100
ORDER BY batting_average DESC;

