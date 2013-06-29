import time
 
class MTC:
        """
	Usage:
	>>> x = MTC()
	>>> x.setProps()
	"""
	def setProps(self):
		date = time.asctime()
		self.date = date
		place = raw_input("Where are you?: ")
		self.place = place
		context = raw_input("What is the current Context?: ")
		self.context = context
		qualia = []
		for i in range(3):
			qualia.append(raw_input("Qualify situation: "))
		self.qualia = qualia
