-- Create database hbtn_0d_usa and table states
-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- create table
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(256) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE (name)
);
