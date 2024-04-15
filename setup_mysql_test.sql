-- Use the mysql database to manage users and permissions
USE mysql;

-- Create the 'hbnb_test_db' database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create the 'hbnb_test' user with a password if it doesn't already exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on 'hbnb_test_db' to the user 'hbnb_test'
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT on 'performance_schema' to the user 'hbnb_test'
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Apply the new permissions
FLUSH PRIVILEGES;
