-- tv shows by genre ids
SELECT tv_show.title, tv_show_genres.genre_id FROM tv_shows JOIN tv_show_genres ON tv_show.id= tv_show_genres.show_id