-- This script will prepare the MySQL server for the project
-- Create the database 'hbnb_dev_db' if it does not exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the user 'hbnb_dev'@'localhost' with password 'hbnb_dev_pwd' if it does not exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on the 'hbnb_dev_db' database to the user 'hbnb_dev'@'localhost'
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant 'SELECT' privilege on the 'performance_schema' database to the user 'hbnb_dev'@'localhost'
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Flush the privileges so the changes take effect
FLUSH PRIVILEGES;
