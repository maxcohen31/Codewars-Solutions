SELECT demographics.id, 
  ASCII(SUBSTRING(demographics.name, 1, 2)) AS name,
  demographics.birthday,
  ASCII(SUBSTRING(demographics.race, 1, 2)) AS race
FROM demographics;