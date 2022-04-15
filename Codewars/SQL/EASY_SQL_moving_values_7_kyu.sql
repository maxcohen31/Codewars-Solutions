/*  SQL  */
SELECT LENGTH(monsters.name) AS id, 
  LENGTH(CAST(monsters.legs AS varchar(10))) AS name,
  LENGTH(CAST(monsters.arms AS varchar(10))) AS legs,
  LENGTH(monsters.characteristics) AS arms,
  LENGTH(CAST(monsters.id AS varchar(10))) AS characteristics
FROM monsters;