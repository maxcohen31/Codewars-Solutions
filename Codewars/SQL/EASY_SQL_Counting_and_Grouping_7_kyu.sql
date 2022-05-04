SELECT demographics.race AS race, COUNT(demographics.race) AS count
FROM demographics
GROUP BY demographics.race
ORDER BY count DESC;