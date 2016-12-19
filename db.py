import os
import psycopg2
import urllib.parse
import bcrypt

# urlparse.uses_netloc.append("postgres")
url = urllib.parse.urlparse(os.environ.get("DATABASE_URL", "postgresql://localhost/texting"))
def connect():

    conn = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
        )
    return conn

def deleteEvents():
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

def registerEvent(t1, t2, dt, type):
    """Adds a new event to the Schedule database.

    The database assigns a unique serial id number for the event.

    Args:
      Team1, team2, datetime, and event type(clan war, arcade night, etc.).
    """
    DB = connect()
    cursor = DB.cursor()
    cursor.execute("INSERT INTO events (team1, team2, datetime, type) VALUES ( %s , %s , %s , %s );",
    (t1, t2, dt, type))
    DB.commit()
    DB.close()
    print("Event",type,"added")

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

def countUser():
    DB = connect()
    cursor = DB.cursor()
    cursor.execute("SELECT count(*) as num FROM users;")
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
    (email, username, bcrypt.hashpw(password,bcrypt.gensalt())))
    DB.commit()
    DB.close()
    print(username,"registered.")

def allNumbers():
    DB = connect()
    cursor = DB.cursor()
    cursor.execute("SELECT * FROM numbers;")
    teams = cursor.fetchall()
    DB.commit()
    DB.close()
    return teams
