#--- test two strings equal? ---#

# the first method
class Word():
	def __init__(self, text):
		self.text = text

	def equal(self, word2):
		return self.text.lower() == word2.text.lower()

# the second method
class Word2():
	def __init__(self, text):
		self.text = text
	
	def __eq__(self, word2):
		return self.text.lower() == word2.text.lower()

#--------------------OTHER OPERATOR -------------------------#
#
#	__ne__(self, other)			self != other
#	__lt__(self, other)			self <  other
#	__gt__(self, other)			self >  other
#	__le__(self, other)			self <= other
#	__ge__(self, other)			self >= other
#
#	__add__(self, other)			self +  other
#	__sub__(self, other)			self -  other
#	__mul__(self, other)			self *  other
#	__floordiv__(self, other)		self // other
#	__truediv__(self, other)		self /  other
#	__mod__(self, other)			self %  other
#	__pow__(self, other)			self ** other
#
#	__str__(self)		str(self)
#	__repr__(self)		repr(self)
#	__len__(self)		len(self)
#
#--------------------OTHER OPERATOR -------------------------#



#-----------------------------TEST-------------------------------------#

# the first method
if __name__ == '__main__':
	print('use A.equal(B) to judge equal')
	first = Word('ha')
	second = Word('HA')
	third = Word('eh')
	print(first.text, 'is equal', second.text, ':',first.equal(second))
	print(first.text, 'is equal', third.text, ':',first.equal(third))
# the second method
	print('------------------\nuse == to judge equal')
	first = Word2('ha')
	second = Word2('HA')
	third = Word2('eh')
	print(first.text, 'is equal', second.text, ':',first == second)
	print(first.text, 'is equal', third.text, ':',first == third)
