def unicode_test(value):
	import unicodedata
	name = unicodedata.name(value)
	value2 = unicodedata.lookup(name)
	print('value = "%s", name = "%s", value2 = "%s"' % (value, name , value2))


#-------------------------MAIN--------------------------#
if __name__ == '__main__':
	unicode_test('A')
	unicode_test("$")
	unicode_test("\u00a2")
	unicode_test('\u20ac')
	unicode_test('\u2603')
	unicode_test('\u00e9')

	# the results of the follow sentences are equal.
	place = 'caf\u00e9'
	print(place)
	place = 'caf\N{LATIN SMALL LETTER E WITH ACUTE}'
	print(place)

	# compute the number of unicode, not the bytes.
	# the results of the follow sentences are equal
	print(len('$'))
	
	print(len('\U0001f47b'))
