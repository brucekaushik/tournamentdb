#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import random
import bleach
from operator import itemgetter


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM match")
    DB.commit()
    DB.close()


def deletePlayers():
    """Remove all the player records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM player")
    DB.commit()
    DB.close()


def countPlayers():
    """Returns the number of players currently registered."""
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT count(player_id) from player")
    playercount = c.fetchall()
    DB.close()

    # print(playercount[0][0])
    return playercount[0][0]


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    name = bleach.clean(str(name))

    DB = connect()
    c = DB.cursor()
    c.execute("INSERT INTO player (name) VALUES (%s)", (name,))
    DB.commit()
    DB.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place,
    or a player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DB = connect()
    c = DB.cursor()
    query = "SELECT player_id, name, " \
            "(SELECT count(winner) FROM match " \
            "WHERE winner=player_id) as wins, " \
            "(SELECT count(*) FROM match " \
            "WHERE winner=player_id OR loser=player_id) as matches " \
            "FROM player ORDER BY wins DESC"
    c.execute(query)
    standings_table = c.fetchall()
    DB.close()

    # standings_table = sorted(standings_table,key=itemgetter(2), reverse=True)
    # print(standings_table)
    return standings_table


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    winner = int(winner)
    loser = int(loser)
    DB = connect()
    c = DB.cursor()
    query = "INSERT INTO match (winner,loser) VALUES (%s,%s)"
    c.execute(query, (winner, loser, ))
    DB.commit()
    DB.close()


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

    # get player standings
    standings = playerStandings()

    # empty list to store the pairs (tuples)
    swissPairs = []

    # build current pair, empty when required
    currentPair = []

    # start the count from 3 for simplicity
    # loop over standings, build tuples, append to swissPairs list
    count = 3
    for standing in standings:
        if(count % 2 != 0):
            currentPair = []
            currentPair.append(standing[0])
            currentPair.append(standing[1])
        else:
            currentPair.append(standing[0])
            currentPair.append(standing[1])
            swissPairs.append(tuple(currentPair))
        count = count+1

    # print(swissPairs)
    return swissPairs


# -----------------------------------------------------
# MAIN PROGRAM ENDS,
# -----------------------------------------------------
# HELPFUL FUNCTIONS (AVOID JUGGLING IN TERMINAL)
# -----------------------------------------------------

def conductMatch(player1, player2):
    player1 = int(player1)
    player2 = int(player2)
    players_in_match = [player1, player2]

    winner = random.choice(players_in_match)

    if winner == players_in_match[0]:
        loser = players_in_match[1]
    else:
        loser = players_in_match[0]

    # print(winner,loser)

    DB = connect()
    c = DB.cursor()
    query = "INSERT INTO match (winner,loser) VALUES (%s,%s)"
    c.execute(query, (winner, loser,))
    DB.commit()
    DB.close()


def viewPlayers():
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT * from player")
    players = c.fetchall()
    DB.close()
    print(players)


def viewMatches():
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT * from match")
    matches = c.fetchall()
    DB.close()
    print(matches)


def registerSpecificPlayer(player_id, name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    player_id = int(player_id)
    name = bleach.clean(str(name))

    DB = connect()
    c = DB.cursor()
    query = "INSERT INTO player (player_id, name) VALUES (%s, %s)"
    c.execute(query, (player_id, name,))
    DB.commit()
    DB.close()


def conductRound():
    pairs = swissPairings()
    for pair in pairs:
        conductMatch(pair[0], pair[2])


def viewPlayerStandings():
    print(playerStandings())


def viewSwissPairings():
    print(swissPairings())

# UNCOMMENT TO FOLLOWING LINES TO CONDUCT ONE ROUND IN THE TOURNAMENT

# deleteMatches()
# deletePlayers()
# registerSpecificPlayer(1, 'kaushik')
# registerSpecificPlayer(2, 'lokesh')
# registerSpecificPlayer(3, 'kishore')
# registerSpecificPlayer(4, 'rakesh')
# registerSpecificPlayer(5, 'saichand')
# registerSpecificPlayer(6, 'patti')
# registerSpecificPlayer(7, 'john')
# registerSpecificPlayer(8, 'ravi')
# viewPlayers()
# conductRound()
# viewMatches()
# viewPlayerStandings()
# viewSwissPairings()
