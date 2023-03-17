#!/usr/bin/python3
"""
This module lists all the cities that we have in our database
"""
import MySQLdb
import sys


if __name__ == "__main__":
    connect = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur=connect.cursor()
    cur.execute("SELECT * FROM cities ORDER BY cities.id ASC")
    inf=cur.fetchall()
    for i in inf:
        print(i)
