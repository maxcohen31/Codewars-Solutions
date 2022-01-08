SELECT 
CASE
    WHEN MOD(SUM(numbers.number1), 2) <> 0 THEN MIN(numbers.number1)
    WHEN MOD(SUM(numbers.number1), 2) = 0 THEN MAX(numbers.number1)
    END AS number1,
CASE    
    WHEN MOD(SUM(numbers.number2), 2) <> 0 THEN MIN(numbers.number2)
    WHEN MOD(SUM(numbers.number2), 2) = 0 THEN MAX(numbers.number2)
    END AS number2
FROM numbers;