SELECT departments.id, departments.name
FROM departments
JOIN sales
  ON departments.id = sales.department_id
WHERE EXISTS(SELECT sales.price FROM sales
           WHERE sales.price > 98.00)
GROUP BY departments.name, departments.id
ORDER BY 1, 2 LIMIT 5;