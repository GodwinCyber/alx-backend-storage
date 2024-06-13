-- Check if the 'users' table exists, and if not, create it
-- 'id' is a unique identifier for each user, automatically incremented
-- 'email' is used to store the user's email address, must be unique
-- 'name' is used to store the user's name
-- 'country' is an enumeration that stores the user's country, defaults to 'US'
-- Define 'id' as the primary key for the table
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id int AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
    PRIMARY KEY (id)
);