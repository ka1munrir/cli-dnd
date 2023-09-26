import sqlite3

CONN = sqlite3.connect('lib/db.db')
CURSOR = CONN.cursor()