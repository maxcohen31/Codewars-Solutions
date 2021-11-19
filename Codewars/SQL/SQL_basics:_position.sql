SELECT monsters.id, monsters.name, POSITION(',' IN characteristics) AS comma
FROM monsters
ORDER BY comma;