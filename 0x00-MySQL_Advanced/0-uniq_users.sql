-- Create table users
-- Auto-incrementing unique identifier for each user
-- User's email address (must be unique and not null)
-- User's full name
-- Define the primary key for the table (id column)
DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id int AUTO_INCREMENT,
  
  email VARCHAR(255) NOT NULL UNIQUE,
  
  name VARCHAR(255),
  
  PRIMARY KEY (id)
);