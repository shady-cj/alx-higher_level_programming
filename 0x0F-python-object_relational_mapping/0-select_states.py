#!/usr/bin/python3

import MySQLdb
import sys

def main(username, password, db_name):
    db = MySQLdb.connect(host='localhost', db=db_name, user=username, passwd=password, port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM STATES")
    cursor.fetchall()
    cursor.close()
    db.close()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
