-- Database: tournament

--DROP DATABASE tournament;

--CREATE DATABASE tournament
--  WITH OWNER = postgres
--       ENCODING = 'UTF8'
--       TABLESPACE = pg_default
--       LC_COLLATE = 'English_United States.1252'
--       LC_CTYPE = 'English_United States.1252'
--       CONNECTION LIMIT = -1;



create table players ( id serial PRIMARY KEY, name varchar );

--Add table for each match containing winner and loser 
create table matches ( id serial primary key, winner int  references players(id), loser int references players(id)); 

--Add table for standings containing matches played and total score
create table standings ( id serial PRIMARY KEY, player_id int references players(id), matches_played int, wins int);





