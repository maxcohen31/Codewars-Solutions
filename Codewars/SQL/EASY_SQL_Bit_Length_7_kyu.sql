SELECT 
  demographics.id,
  BIT_LENGTH(demographics.name) AS name,
  demographics.birthday,
  BIT_LENGTH(demographics.race) AS race
FROM demographics
ORDER BY id;