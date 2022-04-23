/*  SQL  */
SELECT (BIT_LENGTH(demographics.name) + LENGTH(demographics.race)) AS calculation
FROM demographics