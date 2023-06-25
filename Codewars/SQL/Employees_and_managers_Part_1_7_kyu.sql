-- Substitute with your SQL
SELECT employees.manager_id,
ARRAY_AGG(CONCAT(employees.name, ' (', employees.id, ')') ORDER BY employees.id) AS employee_names
FROM employees
WHERE employees.manager_id IS NOT NULL
GROUP BY employees.manager_id;
