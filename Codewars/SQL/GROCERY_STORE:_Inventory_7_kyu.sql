SELECT products.id, products.name, products.stock
FROM products
WHERE products.stock <= 2 AND products.producent = 'CompanyA'
ORDER BY products.id;