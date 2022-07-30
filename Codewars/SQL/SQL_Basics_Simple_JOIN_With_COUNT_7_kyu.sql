-- Create your SELECT statement here
SELECT people.id, people.name, COUNT(toys.id) AS toy_count
FROM people
  JOIN toys ON people.id = toys.people_id
GROUP BY 1
