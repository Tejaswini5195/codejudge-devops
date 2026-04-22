import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Harshita@3344",   # change if you have password
        database="codejudge"
    )