import re
source = 'Young Frankenstein'
print('source string: ', source)

#-----------------------------------------
# testing from the beginning of the string

m = re.match('You', source)
if m:
	print('match results: ', m.group())

m = re.match('^You', source)
if m:
	print('match results: ', m.group())

#have no output
m = re.match('Frank', source)
if m:
	print('match results: ', m.group())

#-----------------------------------------


#********************************************************
# testing from anywhere of the string

m = re.search('Frank', source)
if m:
	print('search results: ', m.group())

# '.' is one characters, and '*' is any long characters
m = re.search('.*Frank', source)
if m:
	print('search results: ', m.group())

# find the all string of the source string
m = re.findall('n', source)
print('all the characters in source string:', m)

# find the all string of the source string and the '?' 
# express that the character of the '.' expressed can 
# ignore or not ignore,so which can be selected.
m = re.findall('n.?', source)
print('all the characters in source string:', m)

# split('x', source) split the source string by 'x'
m = re.split('n', source)
print('split the source string by "n":',m)

# sub(old, new, source) replace old by new in source
m = re.sub('n', '?', source)
print("replace 'n' by '?' in source string:", m)

#********************************************************


########################## regular expression ###############################
#																		  	#
#	\d			one number												  	#
#	\D			one character and not number							  	#
#	\w			one alphabet or number									  	#
#	\W			one character that is not alphabet and number and underline	#
#	\s			space character											  	#
#	\S			not space character										  	#
#	\b			a boundary between \w and \W, and the order can reverse	  	#
#	\B			not \b													 	#
#																		  	#
########################## regular expression ###############################

import string
printable = string.printable
print('printable:', printable)
print('printable length:', len(printable))

# find the all number in printable
print('find the all number in printable:')
print(re.findall('\d', printable))

# find the all number or alphabet in printable
print('find the all number or alphabet in printable:')
print(re.findall('\w', printable))

# find the space character
print('find the space character:')
print(re.findall('\s', printable))


# regular expression can be used to the Unicode character
print('regular expression can be used to the Unicode character:')
x = 'abc' + '-\*' +'\u00ea' + '\u0115'
print(re.findall('\w', x))

########################## regular expression ##########################################################
#																		  	
#	abc				the text of abc												  	
#	(expr)			expr 
#	expr1 | expr2	expr1 or expr2
#	.				any character except '\n'
#	^				the beginning of the string
#	$				the tail of the string
#	prev?			zero or one prev
#	prev*			zero or many prev, and match more as can as possible
#	prev*?			zero or many prev, and match little as can as possible
#	prev+			one or many prev, and match more as can as possible
#	prev+?			one or many prev, and match little as can as possible
#	prev{m}			has prev consecutively in quantity of m
#	prev{m, n}		has prev consecutively in quantity of from m to n, and match more as can as possible
#	prev{m, n}?		has prev consecutively in quantity of from m to n, and match little as can as possible
#	[abc]			a or b or c(like a|b|c)
#	[^abc]			not (a or b or c)
#	prev(?=next)	if the back of the string is next, return the prev
#	prev(?!next)	if the back of the string is not next , return prev
#	(?<=prev)next	if the front of the string is prev, return next
#	(?<!prev)next	if the front of the string is not prev, return next
#	(?P< name >expr) the mode will match expr and save as name
#
########################## regular expression ###########################################################

source2 = '''I wish I may, I wish I might 
			 Have a dish of fish tonight.'''
print('source2:', source2)

print(re.findall('wish', source2))
print(re.findall('wish|fish', source2))

print(re.findall('^wish', source2))
print(re.findall('^I wish', source2))

print(re.findall('fish$', source2))
print(re.findall('fish tonight.$', source2))
print(re.findall('fish tonight\.$', source2))

print(re.findall('[wf]ish', source2))
print(re.findall('[wsh]+', source2))
print(re.findall('ght\W', source2))

print(re.findall('I (?=wish)', source2))

print(re.findall('(?<=I) wish', source2))

# pay attention to the follw sentences
print(re.findall('\bfish', source2))
print(re.findall(r'\bfish', source2))


# pay attention to the m.group and m.groups
m = re.search(r'(. dish\b).*(\bfish)', source2)
print('m.group = ', m.group())
print('m.groups =', m.groups())

# (?P< name >expr) the mode will match expr and save as name
m = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)', source2)
print('m.group = ', m.group())
print('m.groups =', m.groups())
print('DISH =', m.group('DISH'))
print('FISH =', m.group('FISH'))
