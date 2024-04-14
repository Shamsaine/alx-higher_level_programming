#!/usr/bin/python3

import MySQLdb
import sys

def list_states(username, password, database_name):
    try:
        conn = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database_name)
        cursor = conn.cursor()
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return

    try:
        cursor.execute("SELECT * FROM states ORDER BY states.id")
        states = cursor.fetchall()
    except MySQLdb.Error as e:
        print(f"Error executing SQL query: {e}")
        conn.close()
        return
    
    for state in states:
        print(state)


    conn.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
        list_states(username, password, database_name)

