-- Create your SELECT statement here
SELECT MIN(result.score) AS min,
PERCENTILE_CONT(0.5) WITHIN GROUP(ORDER BY result.score) as median,
MAX(result.score) AS max
FROM result