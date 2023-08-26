-- Substitute with your SQL
SELECT DISTINCT orders.customer_id
FROM orders
WHERE orders.customer_id NOT IN (
    SELECT orders.customer_id
    FROM orders
    WHERE orders.delivery_date IS NOT NULL
)
ORDER BY 1 DESC;
