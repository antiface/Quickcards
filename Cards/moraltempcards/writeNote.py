import os
 
os.chdir('C:\\Refcards')
 
def writeNote(x):
	with open(x, 'w') as outfile:
		outfile.write(raw_input('Write note: '))
		
"""
>>> writeNote('refcards_18Sep14d.txt')
Write note: etc.
 
"""
import time
 
def f():
	t = time.strftime('%Y%m%d%H%M')
	writeNote(t+'.txt')
