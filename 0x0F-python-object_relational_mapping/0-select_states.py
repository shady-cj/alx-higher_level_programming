#!/usr/bin/python3
"""
This module uses MySQLdb to connect to a database passed from the command
line and performs sql operations (CRUD)
"""
import MySQLdb
import sys

def main(username, password, db_name):
    """
    The main function acts as the entry point into the main functionality
    It makes the connection and calls the cursor on the db connection which is
    later used to make sql queries
    """
    db = MySQLdb.connect(host='localhost', db=db_name, user=username, passwd=password, port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    cursor.fetchall()
    cursor.close()
    db.close()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
