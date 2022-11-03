-- create a table with an id field of default value 1 and also unique

CREATE TABLE IF NOT EXISTS unique_id (
	id INT UNIQUE DEFAULT 1,
	name VARCHAR(256)
	);
