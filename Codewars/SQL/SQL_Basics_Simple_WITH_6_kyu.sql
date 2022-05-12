-- CTE
WITH special_sales AS (
SELECT * 
FROM sales
WHERE sales.price > 90
)
SELECT departments.id, departments.name 
FROM departments
JOIN sales
  ON departments.id = sales.department_id
WHERE departments.id IN (SELECT sales.department_id FROM special_sales)
GROUP BY departments.id, departments.name
