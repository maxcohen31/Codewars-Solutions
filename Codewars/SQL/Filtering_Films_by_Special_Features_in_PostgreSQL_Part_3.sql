SELECT film.film_id, film.title, film.special_features
FROM film
WHERE NOT 'Commentaries' = ANY(special_features)
AND ('Behind the Scenes' = ANY(special_features) OR 'Deleted Scenes' = ANY(special_features))
AND NOT ('Behind the Scenes' = ANY(special_features) AND 'Deleted Scenes' = ANY(special_features))
ORDER BY 2, 1;

-- ALternative solution
SELECT film.film_id, film.title, film.special_features
WHERE (special_features @> ARRAY['Deleted Scenes'] AND NOT special_features @> ARRAY['Behind the Scenes'])
OR
special_features @> ARRAY['Behind the Scenes'] AND NOT special_features @> ARRAY['Deleted Scenses']
AND NOT special_features @> ARRAY['Commentaries']
ORDER BY 2, 1;

