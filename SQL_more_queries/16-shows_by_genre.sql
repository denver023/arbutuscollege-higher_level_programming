-- This query lists all shows and their linked genres. If a show has no genre, it displays NULL in the genre column.
SELECT tv_shows.title, tv_genres.name AS genre
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, genre ASC;
