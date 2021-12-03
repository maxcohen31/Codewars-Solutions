SELECT products.name, products.weight, products.price, ROUND((products.price/(products.weight/1000))::numeric, 2)::float AS price_per_kg
FROM products
ORDER BY price_per_kg ASC, products.name ASC;
