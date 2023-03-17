#!/usr/bin/python3
"""
This module lists all the cities in a certain state using the state name
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
    l = []
    cur = connect.cursor()
    cur.execute("SELECT cities.id, cities.name,states.name FROM cities\
                INNER JOIN states ON cities.state_id = \
                states.id ORDER BY cities.id ASC")
    r = cur.fetchall()
    for i in r:
        if i[2] == sys.argv[4]:
            l.append(i[1])
    for i in range(len(l)):
        if i == len(l) - 1:
            print(l[i])
        else:
            print(l[i], end=" ,")
