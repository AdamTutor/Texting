import os
import psycopg2
import urllib.parse
import bcrypt
from flask_login import UserMixin


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


class Event:
    def __init__(self, team1, team2, datetime, event_type):
        self.team1 = team1
        self.team2 = team2
        self.datetime = datetime
        self.event_type = event_type

    def deleteEvents():
        """Remove all the events from the database."""
        DB = connect()
        cursor = DB.cursor()
        cursor.execute("DELETE FROM events;");
        DB.commit()
        DB.close()
        print("all Events deleted")

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

    def create(t1,t2,dt,type):
        DB = connect()
        cursor = DB.cursor()
        cursor.execute("INSERT INTO events (team1, team2, datetime, type) VALUES ( %s , %s , %s , %s );",
        (t1, t2, dt, type))
        DB.commit()
        DB.close()
        print("Event",type,"added")

    @staticmethod
    def count():
        DB = connect()
        cursor = DB.cursor()
        cursor.execute("SELECT count(*) as num FROM events;")
        result = int(cursor.fetchone()[0])
        DB.close()
        return result

    @staticmethod
    def delete(id):
        DB = connect()
        cursor = DB.cursor()
        cursor.execute("DELETE FROM events WHERE id = (%s);",(id,));
        DB.commit()
        DB.close()
        print("all events deleted")

class Team:
    def __init__(self, id, name):
        self.id = id
        self.name = name


    def create(name):
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

    def allTeams():
        DB = connect()
        cursor = DB.cursor()
        cursor.execute("SELECT * FROM teams;")
        teams = cursor.fetchall()
        DB.commit()
        DB.close()
        return teams

    @staticmethod
    def count():
        DB = connect()
        cursor = DB.cursor()
        cursor.execute("SELECT count(*) as num FROM teams;")
        result = int(cursor.fetchone()[0])
        DB.close()
        return result

    @staticmethod
    def delete(id):
        DB = connect()
        cursor = DB.cursor()
        cursor.execute("DELETE FROM teams WHERE id = (%s);",(id,));
        DB.commit()
        DB.close()
        print("all teams deleted")

class User(UserMixin):
    def __init__(self, id, email, username, hashedpassword):
        self.id = id
        self.email = email
        self.username = username
        self.hashedpassword = hashedpassword

    def __str__(self):
        return


    


    def create(email, username, password):
        DB = connect()
        cursor = DB.cursor()
        cursor.execute("INSERT INTO users (email, username, password) VALUES ( %s , %s , %s);",
        (email, username, bcrypt.hashpw(password.encode(),bcrypt.gensalt())))
        DB.commit()
        DB.close()
        print(username,"registered.")

    def countUser():
        DB = connect()
        cursor = DB.cursor()
        cursor.execute("SELECT count(*) as num FROM users;")
        result = int(cursor.fetchone()[0])
        DB.close()
        return result

    @staticmethod
    def hashedpassword(name):
        DB = connect()
        cursor = DB.cursor()
        cursor.execute("SELECT password FROM users WHERE username = (%s);",(name,))
        hashedpassword = cursor.fetchall()
        DB.close()
        return hashedpassword

    @staticmethod
    def getall():
        DB = connect()
        cursor = DB.cursor()
        cursor.execute("SELECT * FROM users;")
        users = [User(*row) for row in cursor.fetchall()]
        DB.close()
        return users

    @staticmethod
    def get(id):
        DB = connect()
        cursor = DB.cursor()
        cursor.execute("SELECT * FROM users WHERE id =(%s);",(id,))
        user = User(*cursor.fetchone())
        DB.close()
        return user

    @staticmethod
    def getByUsername(username):
        DB = connect()
        cursor = DB.cursor()
        cursor.execute("SELECT User FROM users WHERE username =(%s) "),(username,)
        user = User(*cursor.fetchone())
        DB.close()
        return user



class Phone_number:
    def __init__(self, user, phone_number):
        self.user = user
        self.phone_number = phone_number
















# urlparse.uses_netloc.append("postgres")










def allNumbers():
    DB = connect()
    cursor = DB.cursor()
    cursor.execute("SELECT * FROM numbers;")
    teams = cursor.fetchall()
    DB.commit()
    DB.close()
    return teams
