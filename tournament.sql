-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- drop tournament database if it exists
DROP DATABASE IF EXISTS tournament;

-- create tournament database
CREATE DATABASE tournament;

\connect tournament

-- drop tables if they exist
-- DROP TABLE IF EXISTS player CASCADE;
-- DROP tABLE IF EXISTS match CASCADE;

-- create player table
CREATE TABLE player (
	player_id serial,
	name text,
	PRIMARY KEY (player_id)
);

-- create match table
CREATE TABLE match (
	match_id serial,
	winner integer,
	loser integer,
	PRIMARY KEY(match_id),
	FOREIGN KEY(winner) REFERENCES player(player_id),
	FOREIGN KEY(loser) REFERENCES player(player_id)
);