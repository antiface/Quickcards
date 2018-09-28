import sqlite3
import os
import time

# Choose the filepath you want the database to reside in.
os.chdir('C:\\FILEPATH')

# Creates the database on the first run, otherwise just connects to it.
conn = sqlite3.connect("refcards2019.db")
cursor = conn.cursor()

# To be used on the first "run" to create the first TABLE in the database.
# cursor.execute("""CREATE TABLE refcards(id INTEGER PRIMARY KEY AUTOINCREMENT,
#			date TEXT, note TEXT)""")
# conn.commit()

# A timestamp in a useful format.
t = time.strftime('%Y%m%d%H%M')

# Prompt to write the actual note.
c = raw_input('Write note: ')

# Inserts timestamp and note into the refcards TABLE as a record.
cursor.execute("""INSERT INTO refcards(date, note)
			VALUES(?,?)""", (t,c))

# Operations on database tables must be "committed".
conn.commit()

# I use this to print the contents of the TABLE,
# just to see that it worked properly.
# This section can be skipped.
sql = "SELECT * FROM refcards"
cursor.execute(sql)
print cursor.fetchall()

# Close connection to database.
conn.close()
