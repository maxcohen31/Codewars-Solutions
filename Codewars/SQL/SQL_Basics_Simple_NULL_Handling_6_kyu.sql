-- Create your SELECT statement here
SELECT eusales.id,
  COALESCE(NULLIF(eusales.name, ''), '[product name not found]') AS name,
  eusales.price,
  COALESCE(NULLIF(eusales.card_name, ''), '[card name not found]') AS card_name,
  eusales.card_number,
  eusales.transaction_date
FROM eusales
WHERE price > 50