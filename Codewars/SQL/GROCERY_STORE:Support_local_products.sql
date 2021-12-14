SELECT COUNT(products.id) AS products, products.country
FROM products
WHERE products.country IN ('United State of America', 'Canada')
GROUP BY products.country
ORDER BY products.country DESC;