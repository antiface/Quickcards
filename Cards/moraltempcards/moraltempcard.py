from algorithm import Algorithm
import time
 
def qualia():
	return {'qualia': input("Number from 0 to 100: ")}
 
def t():
	return {'t': time.asctime()}
 
moraltemp = Algorithm(t, qualia)
 
card = moraltemp.run()
# Number from 0 to 100: 49
card['t']
# 'Sat Feb 15 01:37:30 2014'
card['qualia']
# 49
