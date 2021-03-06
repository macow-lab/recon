-- Change names

CREATE DATABASE recondb;

use recondb;

CREATE TABLE user (
	user_id serial primary key,
	username VARCHAR(255) UNIQUE NOT NULL,
	password VARCHAR(30) NOT NULL,
	email VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE budget (
	budget_id VARCHAR(255),
	incomes MONEY,
	expense MONEY,
	savings MONEY,
	investments MONEY,
	categories VARCHAR(255),
	FOREIGN KEY(budget_id) REFERENCES user (username)
);

CREATE TABLE networth (
	networth_id int,
	stamp DATE NOT NULL,
	asset_type ENUM ('Asset', 'Passive'),
	categories VARCHAR(255),
	FOREIGN KEY(networth_id) REFERENCES user (username)
);

-- Dummy data
INSERT INTO user (username, password, email) VALUES ('Sukuna', 'pass', 'admin@recon.com');
