import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import db

def createdb():
    DB = psycopg2.connect(dbname="postgres")
    DB.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = DB.cursor()
    cursor.execute("CREATE DATABASE texting;")
    DB.close()
    print("Success")
    DB = psycopg2.connect(dbname="texting")
    cursor = DB.cursor()
    cursor.execute(open("init.sql").read())
    DB.commit()
    DB.close()
    print("Success")


def recreate_tables():
    DB = db.connect()
    cursor = DB.cursor()
    cursor.execute(open("init.sql").read())
    DB.commit()
    DB.close()
if __name__ == '__main__':
    recreate_tables()
