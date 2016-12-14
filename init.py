import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def createdb():
    DB = psycopg2.connect(dbname="postgres")
    DB.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = DB.cursor()
    cursor.execute("CREATE DATABASE schedule;")
    DB.close()
    print("Success")
    DB = psycopg2.connect(dbname="schedule")
    cursor = DB.cursor()
    cursor.execute(open("init.sql").read())
    DB.commit()
    DB.close()
    print("Success")



createdb()
