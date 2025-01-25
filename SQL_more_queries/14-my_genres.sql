-- This query lists all genres for the show 'Dexter' and sorts them in ascending order by genre name
SELECT tv_genres.name AS genre FROM tv_genres JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id WHERE tv_shows.title = 'Dexter' ORDER BY tv_genres.name ASC;
