-- Use the mysql database to manage users and permissions
USE mysql;

-- Create the 'hbnb_dev_db' database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the 'hbnb_dev' user with a password if it doesn't already exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on 'hbnb_dev_db' to the user 'hbnb_dev'
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT on 'performance_schema' to the user 'hbnb_dev'
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Apply the new permissions
FLUSH PRIVILEGES;
