SELECT *
FROM travelers
WHERE travelers.country NOT IN ('Canada', 'Mexico', 'USA');