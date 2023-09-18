-- Prepares the MySQL server for the project
-- Create the database 'hbnb_test_db' if it does not exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create the user 'hbnb_test'@'localhost' with password 'hbnb_test_pwd' if it does not exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on the 'hbnb_test_db' database to the user 'hbnb_test'@'localhost'
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant 'SELECT' privilege on the 'performance_schema' database to the user 'hbnb_test'@'localhost'
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Flush the privileges so the changes take effect
FLUSH PRIVILEGES;
