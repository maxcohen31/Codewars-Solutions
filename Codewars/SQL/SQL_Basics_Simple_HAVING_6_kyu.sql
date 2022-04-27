-- Create your SELECT statement here
SELECT people.age, COUNT(people.id) AS total_people
FROM people
GROUP BY people.age
HAVING COUNT(people.age) >= 10  