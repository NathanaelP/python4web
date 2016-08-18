#!/usr/bin/env python3
import sqlite3 as db

conn = db.connect('test.db')
cursor = conn.cursor()
cursor.execute('insert into films values("Annie Hall", "1997", "Woody Allen")')
cursor.execute('insert into films values("The Godfather", "1972", "Francis Ford Copala")')

conn.commit()
print("records created successfully.")
conn.close()