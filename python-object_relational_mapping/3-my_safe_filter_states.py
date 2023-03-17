#!/usr/bin/python3
"""
This module is used to list our mysql data using python
"""
import MySQLdb
import sys

if __name__ == "__main__":
    connect = MySQLdb.connect(
        host="localhost",
        port=3360,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY states.id ASC", sys.argv[4])
    row = cursor.fetchall()
    for r in row:
        print(format(r))
