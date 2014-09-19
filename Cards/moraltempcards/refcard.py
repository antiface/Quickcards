import time
 
def refCard():
	x = {"time": time.asctime(), "context": raw_input("What is the context?: "),
	"temp": input("What is the moral temperature?: ")}
	return x
 
def makeCard():
	x = []
	x.append(refCard())
	return x
 
def updateCard():
	x.append(makeCard())
	return x
 
# x = makeCard()
# x = updateCard()
 
"""
x = makeCard()
What is the context?: At home.
What is the moral temperature?: 29
>>> x
[{'temp': 29, 'context': 'At home.', 'time': 'Tue Feb 11 00:49:11 2014'}]
 
"""
