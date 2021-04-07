CREATE DATABASE recondb;

use recondb;

CREATE TABLE user (
	user_id serial primary key,
	username VARCHAR(255) UNIQUE NOT NULL,
	password VARCHAR(50) NOT NULL,
	email VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE budget (
	id serial primary key,
	username VARCHAR(255) NOT NULL,
	stamp DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	incomes DECIMAL(15,2),
	expenses DECIMAL(15,2),
	savings DECIMAL(15,2),
	investments DECIMAL(15,2),
	categories VARCHAR(255),
	FOREIGN KEY(username) REFERENCES user (username)
);

CREATE TABLE networth (
	id serial primary key,
	username VARCHAR(255) NOT NULL,
	stamp DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	asset_type ENUM('Asset', 'Passive'),
	categories VARCHAR(255),
	FOREIGN KEY(username) REFERENCES user (username)
);

INSERT INTO user (username, password, email) VALUES ('Sukuna', 'pass', 'admin@recon.com');
INSERT INTO budget (username, incomes, categories) VALUES ('Sukuna', 1, "Juju");
INSERT INTO budget (username, incomes, categories) VALUES ('Sukuna', 211, "Jujsau");
INSERT INTO budget (username, incomes, categories) VALUES ('Sukuna', -321, "Juasju");
INSERT INTO budget (username, incomes, categories) VALUES ('Sukuna', 4421, "Jujus");
INSERT INTO budget (username, incomes, categories) VALUES ('Sukuna', 55, "Juju1q");
INSERT INTO budget (username, incomes, categories) VALUES ('Sukuna', -22, "Jujewqeqwu");


