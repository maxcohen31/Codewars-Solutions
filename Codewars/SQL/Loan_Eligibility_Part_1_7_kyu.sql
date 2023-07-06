-- Substitute with your SQL
SELECT customers.id AS customer_id,
CASE
  WHEN customers.age >= 18 and customers.age <= 65 AND COUNT(loans.id) = 0 THEN 'loan can be given'
  ELSE 'loan cannot be given'
END AS loan_eligibility
FROM customers
LEFT JOIN loans ON customers.id = loans.id AND loans.loan_status = 'unpaid'
WHERE customers.id >= 1 AND customers.id <= 10
GROUP BY 1
ORDER BY 1 DESC;
