SELECT countries.capital
FROM countries
WHERE countries.continent LIKE '%Afri_a' AND countries.country LIKE 'E%'
ORDER BY countries.capital ASC
LIMIT 3;