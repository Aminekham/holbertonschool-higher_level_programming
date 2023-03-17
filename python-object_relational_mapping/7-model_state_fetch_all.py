#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""
import sqlalchemy
import MySQLdb
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database)

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")

    result = cur.fetchall()
    for row in result:
        print(row[0], end="")
        print(": ", end="")
        print(row[1])