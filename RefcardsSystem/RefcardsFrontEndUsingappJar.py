import os
import sqlite3
from appJar import gui

os.chdir('C:\\FILEPATH')

# TO RUN ON FIRST PASS, TO CREATE OR OPEN DATABASE AND CREATE FIRST TABLE.
# conn = sqlite3.connect("refcards2019b.db")
# cursor = conn.cursor()
# cursor.execute("""CREATE TABLE refcards(date TEXT, note TEXT)""")
# conn.commit()

app=gui()

app.addLabelEntry("Time")
app.addTextArea("Note", text=None)

def insert(date,note):
	conn = sqlite3.connect("refcards2019b.db")
	cursor = conn.cursor()
	cursor.execute("INSERT INTO refcards VALUES (?,?)",(date, note))
	conn.commit()
	conn.close()

def add_entry():
	insert(app.getEntry("Time"), app.getTextArea("Note"))

app.addButton("Add entry", add_entry)

app.go()
