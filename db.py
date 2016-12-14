
import psycopg2
import validation.py

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=Texting")

def deleteEvent():
    """Remove all the events from the database."""
    DB = connect()
    cursor = DB.cursor()
    cursor.execute("DELETE FROM events;");
    DB.commit()
    DB.close()
    print("all Events deleted")

def deleteTeams():
    """delete teams from teams table in database"""
    DB = connect()
    cursor = DB.cursor()
    cursor.execute("DELETE FROM teams;");
    DB.commit()
    DB.close()
    print("all teams deleted")

def countEvents():
    """Returns the number of events currently registered."""
    DB = connect()
    cursor = DB.cursor()
    cursor.execute("SELECT count(*) as num FROM events;")
    result = int(cursor.fetchone()[0])
    DB.close()
    return result


def countTeams():
    DB = connect()
    cursor = DB.cursor()
    cursor.execute("SELECT count(*) as num FROM teams;")
    result = int(cursor.fetchone()[0])
    DB.close()
    return result

def registerUser(email, username, password):
    """Adds a new event to the Schedule database.

    The database assigns a unique serial id number for the event.

    Args:
      Team1, team2, datetime, and event type(clan war, arcade night, etc.).
    """
    DB = connect()
    cursor = DB.cursor()
    cursor.execute("INSERT INTO users (email, username, password) VALUES ( %s , %s , %s);",
    (email, username, password))
    DB.commit()
    DB.close()
    print(username,"registered.")

def registerTeam(name):
    """Adds a new team to the database."""
    DB = connect()
    cursor = DB.cursor()
    cursor.execute("INSERT INTO teams (name) VALUES (%s);",
    (name,))
    DB.commit()
    DB.close()
    print("Team",name,"added")
    DB = connect()
    cursor = DB.cursor()
    cursor.execute("SELECT id FROM teams WHERE name = %s;",(name,))
    ans = cursor.fetchone()[0]
    DB.commit()
    DB.close()
    print(ans)
    return ans

def allEvents():
    DB = connect()
    cursor = DB.cursor()
    cursor.execute("""SELECT t1.name, t2.name, e.datetime, e.type FROM events e
                      JOIN teams t1 on t1.id = e.team1
                      JOIN teams t2 on t2.id = e.team2
                      ORDER BY datetime ;""")
    events = cursor.fetchall()
    DB.commit()
    DB.close()
    return events

def allTeams():
    DB = connect()
    cursor = DB.cursor()
    cursor.execute("SELECT * FROM teams;")
    teams = cursor.fetchall()
    DB.commit()
    DB.close()
    return teams
