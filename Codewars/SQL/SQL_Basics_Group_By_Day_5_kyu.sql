SELECT DATE(created_at) AS day, COUNT(id) AS count, description  
FROM events
WHERE name = 'trained'
GROUP BY day, description
