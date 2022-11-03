-- a script that shows the genres in the database and the number of shows linked


SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows FROM tv_genres JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id GROUP BY tv_genres.name ORDER BY number_of_shows DESC;
