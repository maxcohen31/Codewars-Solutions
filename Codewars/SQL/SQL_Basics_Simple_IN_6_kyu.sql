SELECT departments.id AS id, departments.name AS name
FROM departments
WHERE departments.id IN (SELECT sales.department_id
                          FROM sales
                          WHERE sales.price > 98.00
                          );
                    