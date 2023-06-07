-- Create your SELECT statement here
SELECT RANK() OVER(ORDER BY SUM(people.points) DESC) AS rank,
CASE
  WHEN (clan IS NULL) OR (clan='') THEN '[no clan specified]' ELSE clan END AS clan,
SUM(people.points) AS total_points,
COUNT(DISTINCT(people.name)) AS total_people
FROM people
GROUP BY 2
ORDER BY 3 DESC;
