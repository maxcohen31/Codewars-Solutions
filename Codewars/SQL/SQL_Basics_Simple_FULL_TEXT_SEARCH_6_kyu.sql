SELECT product.id, product.name, product.price
FROM product
WHERE to_tsvector(product.name) @@ to_tsquery('Awesome');

