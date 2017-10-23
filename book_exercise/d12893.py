def tester(start):
	state=start
	def nested(label):
		print(label,state)
	return nested

