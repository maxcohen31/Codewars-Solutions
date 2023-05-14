-- Your SQL
SELECT film.film_id, film.title, film.special_features
FROM film
WHERE 'Trailers' = ANY(film.special_features) AND 'Deleted Scenes' = ANY(film.special_features)
ORDER BY 2, 1 ASC;
