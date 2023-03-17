-- counting shows for each genre
SELECT g.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres g
JOIN tv_shows_genres sg ON g.id = sg.genre_id
GROUP BY g.id
ORDER BY number_of_shows DESC;