class Duck():
	def __init__(self, input_name):
		self.__name = input_name
	@property # attention the key word
	def name(self):
		print('inside the getter')
		return self.__name

	# attention the key word and the line 16 ~ 19
	@name.setter
	def name(self, input_name):
		print('inside the setter')
		self.__name = input_name

if __name__ == '__main__':
	fowl = Duck('Howard')
	print('fowl.name = ', fowl.name)
	fowl.name = 'Donald'
	print('fowl.name = ', fowl.name)
	
	# The follow access will cause a wrong, and 
	# the __name is the hidden property, which 
	# can't access
	try:
		print('fowl.__name = ', fowl.__name)
	except:
		print("fowl.__name can't access directly")
	# The hidden property can be accessed by this
	print('fowl._Duck__name = ', fowl._Duck__name)
