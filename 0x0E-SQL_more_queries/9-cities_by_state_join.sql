-- script that lists all cities contained in the database hbtn_0d_usa.


SELECT cities.id, cities.name FROM cities INNER JOIN state.name ON state.id = cities.state_id ORDER BY cities.id
