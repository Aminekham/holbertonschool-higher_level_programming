#!/usr/bin/python3
import MySQLdb
import sys
"""
This module is used to list our mysql data using python
"""
connect = MySQLdb.connect(host = "localhost", port = 3360, user = sys.argv[0], passwd = sys.argv[1], db = sys.argv[2])
cursor = connect.cursor()
cursor.excute("SELECT states.id FROM states ORDER BY states.id ASC")
row = cursor.fetchall()
for r in row:
    print(r)