import time
qualia = []
adict = {}
 
def qualiaFunc():
	adict = {'situation':{'date': time.asctime(),
'place': raw_input("Where are you?: "), 'context': raw_input("What is the current Context?: ")}}
	def setQualia():
		for i in range(3):
			qualia.append(raw_input("Qualify situation: "))
		return qualia
	def addQualiaToDict(adict):
		x = setQualia()
		adict.update({'qualia': x})
	addQualiaToDict(adict)
	return adict
 
adict = qualiaFunc()
