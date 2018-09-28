import sqlite3
import os
from Tkinter import *

root = Tk()
S = Scrollbar(root)
T = Text(root, height=8, width=75)
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)

os.chdir('C:\\FILEPATH')

conn = sqlite3.connect("refcards2019.db")
cursor = conn.cursor()

sql = "SELECT * FROM refcards"
cursor.execute(sql)

# note = cursor.fetchone()[2]
note = cursor.fetchall()[1][2]

T.insert(END, note)
mainloop(  )

conn.close()
