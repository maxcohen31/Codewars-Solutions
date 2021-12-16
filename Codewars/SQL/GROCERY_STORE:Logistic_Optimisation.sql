SELECT COUNT(products.producer) AS count_products_types, products.producer
FROM products
GROUP BY products.producer
ORDER BY count_products_types DESC;