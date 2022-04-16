SELECT products.name as product_name, 
  CAST(EXTRACT(YEAR FROM sales.date) AS INTEGER) AS year, 
  CAST(EXTRACT(MONTH FROM sales.date) AS INTEGER) AS month, 
  CAST(EXTRACT(DAY FROM sales.date) AS INTEGER) AS day, 
  SUM(sales_details.count * products.price) AS total
FROM products LEFT JOIN sales_details ON products.id = sales_details.product_id
LEFT JOIN sales ON sales_details.sale_id = sales.id
GROUP BY product_name, ROLLUP(year, month, day)
ORDER BY product_name, year, month, day;