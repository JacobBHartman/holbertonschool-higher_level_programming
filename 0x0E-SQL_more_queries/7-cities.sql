-- create a table on a MySQL server
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
state_id INT NOT NULL,
FOREIGN KEY sid_fk(state_id) REFERENCES states(id),
name VARCHAR(256) NOT NULL);
