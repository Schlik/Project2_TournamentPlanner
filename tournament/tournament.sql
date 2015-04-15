-- Create database
create database tournament;

--Add table for players
create table players 
(
id serial PRIMARY KEY,
name varchar 
);

--Add table for each match containing winner and loser 
create table match
(
id serial primary key,
winner int  references player(id),
loser int references player(id)
);

--Add table for standings containing matches played and total score
create table standings
(
id serial PRIMARY KEY,
id int as players(id), 
matches_played int,
wins int
);




