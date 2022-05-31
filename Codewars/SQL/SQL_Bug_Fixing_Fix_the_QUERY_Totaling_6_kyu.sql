SELECT 
  s.transaction_date::date AS day,
  d.name AS department,
  COUNT(s.id)::integer AS sale_count
FROM department d
JOIN sale s 
  ON d.id = s.department_id
GROUP BY day, d.name
ORDER BY 1, 2 ASC;