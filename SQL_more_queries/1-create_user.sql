-- Create user_0d_1 with all privileges
-- create user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- grant all privileges
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
