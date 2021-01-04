-- Change names

CREATE DATABASE recondb;

use recondb;

CREATE TABLE user (
	user_id serial primary key,
	username VARCHAR(255) UNIQUE NOT NULL,
	password VARCHAR(30) NOT NULL,
	email VARCHAR(255) UNIQUE NOT NULL,
);

CREATE TABLE budget (
	budget_id int,
	income FLOAT(10,2),
	expense FLOAT(10,2),
	saving FLOAT(10,2),
	category VARCHAR(255),
	FOREIGN KEY(budget_id) REFERENCES user (user_id)
);

CREATE TABLE networth (
	networth_id int,
	date DATE NOT NULL,
	FOREIGN KEY(budget_id) REFERENCES user (user_id)
);