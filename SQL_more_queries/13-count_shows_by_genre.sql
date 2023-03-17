SELECT g.name AS genre, COUNT(*) AS number_of_shows
FROM genres g
JOIN shows_genres sg ON g.id = sg.genre_id
GROUP BY g.id
ORDER BY number_of_shows DESC;