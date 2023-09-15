#!/usr/bin/python3
"""
return all table values (table 'states')
parameters given to script: username, password, database
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port="3306",
        user=argv[1],
        passwd=argv[2],
        d=argv[3],
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
