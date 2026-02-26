-- Create database hbtn_0d_2 and user_0d_2 with SELECT privilege only
-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- create user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- grant select on db
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
