class Duck():
	def __init__(self, input_name):
		self.hidden_name = input_name
	@property # attention the key word
	def name(self):
		print('inside the getter')
		return self.hidden_name

	# attention the key word and the line 16 ~ 20
	@name.setter
	def name(self, input_name):
		print('inside the setter')
		self.hidden_name = input_name

if __name__ == '__main__':
	fowl = Duck('Howard')
	print('fowl.name = ', fowl.name)
	fowl.name = 'Donald'
	print('fowl.name = ', fowl.name)
	print('fowl.hidden_name = ', fowl.hidden_name)
