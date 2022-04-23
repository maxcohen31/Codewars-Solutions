SELECT 'US' AS location, 
  ussales.id, 
  ussales.name, 
  ussales.price, 
  ussales.card_name,
  ussales.card_number,
  ussales.transaction_date
FROM ussales
WHERE ussales.price > 50.00
UNION ALL
SELECT 'EU' AS location, 
  eusales.id, 
  eusales.name, 
  eusales.price, 
  eusales.card_name,
  eusales.card_number,
  eusales.transaction_date
FROM eusales
WHERE eusales.price > 50.00
ORDER BY location DESC;

-- Alternative Solution
ALTER TABLE ussales
    ADD COLUMN location VARCHAR(200)
    DEFAULT 'US';

ALTER TABLE eusales
    ADD COLUMN location VARCHAR(200)
    DEFAULT 'EU';

SELECT * FROM ussales
    WHERE price > 50.00
    
UNION ALL

SELECT * FROM eusales
    WHERE price > 50.00
    
ORDER BY location DESC;

