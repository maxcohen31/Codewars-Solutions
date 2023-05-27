-- Your SQL
SELECT film.film_id, film.title, film.special_features
FROM film
WHERE ARRAY['Trailers', 'Deleted Scenes'] <@ film.special_features AND array_length(film.special_features, 1) = 2
ORDER BY 2, 1 ASC;
