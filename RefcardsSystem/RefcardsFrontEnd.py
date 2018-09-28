from Tkinter import *
import os
import sqlite3

os.chdir('C:\\FILEPATH')

# TO RUN ON FIRST PASS, TO CREATE OR OPEN DATABASE AND CREATE FIRST TABLE.
# conn = sqlite3.connect("refcards2019b.db")
# cursor = conn.cursor()
# cursor.execute("""CREATE TABLE refcards(date TEXT, note TEXT)""")
# conn.commit()

def insert(date,note):
	conn = sqlite3.connect("refcards2019b.db")
	cursor = conn.cursor()
	cursor.execute("INSERT INTO refcards VALUES (?,?)",(date, note))
	conn.commit()
	conn.close()
	
def add_command():
	insert(date_text.get(), T.get("1.0","end-1c"))

root = Tk()

date_label = Label(root, text='Date')
date_label.grid(row=0, column=0)

date_text = StringVar()
date_entry = Entry(root, textvariable=date_text)
date_entry.grid(row=0, column=1)

note_label = Label(root, text='Note')
note_label.grid(row=1, column=0)

T = Text(root, height=20, width=20)
T.grid(row=2, column=1)

add_button = Button(root, text="Add entry", width=12, command=add_command)
add_button.grid(row=4, column=3)

root.mainloop()
