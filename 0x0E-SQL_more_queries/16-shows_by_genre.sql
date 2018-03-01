-- lists all shows and all genres linked to those shows
SELECT tv_shows.title, tv_genres.name
FROM tv_show_genres
RIGHT JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
RIGHT JOIN tv_shows
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
