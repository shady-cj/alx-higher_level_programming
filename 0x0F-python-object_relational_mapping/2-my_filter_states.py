#!/usr/bin/python3
"""
This module uses MySQLdb to connect to a database passed from the command
line and performs a search on the database db_name for states
with names equal to the name passed at command line.
"""
import MySQLdb
import sys


def main(username, password, db_name, keyword):
    """
    The main function acts as the entry point into the main functionality
    It makes the connection and calls the cursor on the db connection which is
    later used to make sql queries
    """
    db = MySQLdb.connect(host='localhost', db=db_name, user=username,
                         passwd=password, port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE BINARY states.name='{key}' \
ORDER BY states.id ASC".format(key=keyword))
    for entry in cursor.fetchall():
        print(entry)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
