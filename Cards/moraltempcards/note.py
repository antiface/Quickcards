import os
import time
 
os.chdir('C:\\Refcards')
 
def writeNote(x):
	with open(x, 'w') as outfile:
		outfile.write('Time: '+time.asctime())
		outfile.write('\n')
		outfile.write('\n')
		outfile.write('Context: '+raw_input('Context: '))
		outfile.write('\n')
		outfile.write('\n')
		outfile.write('Qualia: '+raw_input('Qualia: '))
		outfile.write('\n')
		outfile.write('\n')
		outfile.write('Note: '+raw_input('Write note: '))
		
def note():
	t = time.strftime('%Y%m%d%H%M')
	writeNote(t+'.txt')
	
"""
>>> note()
Context: Sitting at home.
Qualia: Having fun.
Write note: Writing notes.

"""
