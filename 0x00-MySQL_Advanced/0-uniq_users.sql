-- Create table users
-- Auto-incrementing unique identifier for each user
-- User's email address (must be unique and not null)
-- User's full name
-- Define the primary key for the table (id column)
CREATE TABLE IF NOT EXISTS users (
  id int AUTO_INCREMENT,
  
  email varchar(255) NOT NULL UNIQUE,
  
  name varchar(255),
  
  PRIMARY KEY (id)
);