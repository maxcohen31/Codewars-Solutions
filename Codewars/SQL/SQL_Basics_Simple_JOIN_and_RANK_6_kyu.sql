SELECT people.id, people.name, COUNT(sales.price) as sale_count,
RANK () OVER (ORDER BY COUNT(sales.price)) as sale_rank
FROM people
JOIN sales
  ON people.id = sales.people_id
GROUP BY 1, 2