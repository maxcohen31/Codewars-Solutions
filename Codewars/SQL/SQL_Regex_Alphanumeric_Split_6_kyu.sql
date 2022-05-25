SELECT repositories.project,
REGEXP_REPLACE(repositories.address, '\d+', '', 'g') AS letters,
REGEXP_REPLACE(repositories.address, '[a-zA-Z]+', '', 'g') AS numbers
FROM repositories

-- Alternative Solution
SELECT 
  project,
  TRANSLATE(address, '1234567890', '') as letters,
  TRANSLATE(address, 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', '') as numbers
FROM repositories;