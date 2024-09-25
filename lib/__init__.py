# lib/config.py
import sqlite3

# Define the path to your database
DATABASE_PATH = 'company.db'

# Establish a connection to the SQLite database
CONN = sqlite3.connect(DATABASE_PATH)
CURSOR = CONN.cursor()

# Optional: Function to close the database connection
def close_connection():
    CURSOR.close()
    CONN.close()
