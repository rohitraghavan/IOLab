-- Insert code to create Database Schema
-- This will create your .db database file for use
DROP TABLE IF EXISTS users;
CREATE TABLE users (
	user_name TEXT PRIMARY KEY,
	password TEXT
);

DROP TABLE IF EXISTS trips;
CREATE TABLE trips (
	trip_name TEXT PRIMARY KEY,
	destination TEXT,
	friend1 TEXT REFERENCES users(user_name),
	friend2 TEXT REFERENCES users(user_name)
);