import csv
import time

t = time.strftime('%Y%m%d%H%M')

with open(t+'.csv', 'wb') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(['Time', 'Context', 'Notes', 'References'])
	writer.writerow([time.asctime(), raw_input('Context: '), raw_input('Notes: '), raw_input('References: ')])
	csvfile.close()
