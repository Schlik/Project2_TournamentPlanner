#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


"""Connect to the PostgreSQL database.  Returns a database connection."""
def connect():
    return psycopg2.connect("dbname=tournament").cursor()

def dc(): 
    return psycopg2.close()


"""Remove all the match records from the database."""
def deleteMatches():
    cursor = connect() 
    query = "delete from matches;"
    cursor.execute( query )
    cursor.commit()  
    dc()
    


"""Remove all the player records from the database."""
def deletePlayers():
    cursor = connect() 
    query = "delete from players;"
    cursor.execute( query )
    cursor.commit()
    dc()


"""Returns the number of players currently registered."""
def countPlayers():
    cursor = connect() 
    query = "select count(*) from players;"
    cursor.execute( query )
    result = cursor.fetchall()
    dc()
    return result[0]


"""Adds a player to the tournament database.
def registerPlayer(input_name):
    cursor = connect() 
    query = "insert into players (name) values (name);"
    cursor.execute( query )
    cursor.commit()
    dc()
  
def playerStandings():
    cursor = connect() 
    query = "select standings.id, players.name, standings.wins, standings.matches_played " +
            " from standings join players order by standings.wins;"
    cursor.execute( query )
    results = cursor.fetchall()
    dc()
    return results;
  
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """


def reportMatch(winner, loser):
    cursor = connect() 
    query = "insert into matches (winner, loser) values (input_winner, input_loser);"
    cursor.execute( query )
    cursor.commit()
    dc()
  
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """


