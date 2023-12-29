-- This sql script prepares a mySQL server for the project
-- by creating a db, configuring username and password
-- and settting up priviledges

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- creating user and configuring username and password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';

-- granting all privileges on hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- granting select privileges on performance_schema db
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- flush priveleges to apply changes
FLUSH PRIVILEGES;
