/*  SQL  */
SELECT demographics.id, demographics.name, demographics.birthday, LOWER(demographics.race) AS race 
FROM demographics