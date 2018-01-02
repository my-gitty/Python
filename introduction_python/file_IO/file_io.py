#!python3
# coding utf-8

##################################################################################
# fileobj = open(filename, mode)
#
# for the first byte of the mode
#
#	mode		description
#	r			read
#	w			write
#	x			if the file not exist, then make new file
#	a			if the file exist, then append contents in the tail of the file
#
# for the second byte of the mode
#
#	t(or ignore)		express the ascii text
#	b					express binary file 
#	
##################################################################################
poem = '''	
			# fileobj = open(filename, mode)
			#
			# for the first byte of the mode
			#
			#	mode		description
			#	r			read
			#	w			write
			#	x			if the file not exist, then make new file
			#	a			if the file exist, then append contents in the tail of the file
			#
			# for the second byte of the mode
			#
			#	t(or ignore)		express the ascii text
			#	b					express binary file 
			#	
	  '''
#----------------- write -----------------#

# the first mothod to write to a file
fout = open('relativity.dean', 'wt')
length = fout.write(poem)
print('write characters:', length)
fout.close()

# previous example is equal to follow
fout = open('relativity.dean', 'wt')
print(poem, file=fout)
fout.close()

# previous example is equal to follow
fout = open('relativity.dean', 'wt')

# sep express remove the space
# end express remove the blank newline
print(poem, file=fout, sep = '', end = '')
fout.close()



#----------------- read -----------------#

fin = open('relativity.dean', 'rt')
poem2 = fin.read()
fin.close()
print('read  characters:', len(poem2))

poem3 = ''
fin = open('relativity.dean', 'rt')
chunk = 100
while True:
	fragment = fin.read(chunk)
	if not fragment:
		break
	poem3 += fragment

fin.close()
print('read  characters:', len(poem3))


#----------------- readline -----------------#

poem4 = ''
fin = open('relativity.dean', 'rt')

while True:
	line = fin.readline()
	if not line:
		break
	poem4 += line

fin.close()
print('readline characters:', len(poem4))



#----------------- iterator -----------------#

poem5 = ''
fin = open('relativity.dean', 'rt')

for line in fin:
	poem5 += line

fin.close()
print('iterator read characters:', len(poem5))

#---------------- with ... as ---------------#
# the method can close file auto

with open('relativity.dean', 'wt') as fout:
	fout.write(poem)

#----------------- binary file -----------------#

# just like the ascii file
bdata = bytes(range(0, 256))
fout = open('bfile.dean', 'wb')
fout.write(bdata)
fout.close()

fin = open('bfile.dean', 'rb')
# tell() return the offset from the file start
fin.tell()
# seek() set the offset from the file start
fin.seek(255)
bdata = fin.read()
print(len(bdata))
fin.close()

#########################################################################
#	
#	seek(offset, origin)
#
#	if origin == 0(defaut), then set the offset from header of the file
#	if origin == 1, then set the offset from current of the file
#	if origin == 2, then set the offset from tail of the file
#
#########################################################################



#----------------- CSV file -----------------#


import csv
villains = [
			['Doctor', 'No'],
			['Rosa', 'Kelebb'],
			['Mister', 'Big'],
			['Auric', 'Goldfinger'],
			['Ernst', 'Blofeld'],
		   ]
with open('villains.dean', 'wt') as fout:
	csvout = csv.writer(fout)
	csvout.writerows(villains)


with open('villains.dean', 'rt') as fin:
	cin = csv.reader(fin)
	villains = [row for row in cin]
print(villains)


with open('villains.dean', 'rt') as fin:
	cin = csv.DictReader(fin, fieldnames = ['first', 'last'])
	villains = [row for row in cin]
print(villains)

villains2 = [
				{'first': 'Doctor', 'last': 'No'}, 
				{'first': 'Rosa', 'last': 'Kelebb'}, 
				{'first': 'Mister', 'last': 'Big'}, 
				{'first': 'Auric', 'last': 'Goldfinger'}, 
				{'first': 'Ernst', 'last': 'Blofeld'}
			]

with open('villains2.dean', 'wt') as fout:
	cout = csv.DictWriter(fout, ['first', 'last'])
	cout.writeheader()
	cout.writerows(villains2)

with open('villains2.dean', 'rt') as fin:
	cin = csv.DictReader(fin)
	villains = [row for row in cin]
print(villains)



#----------------- xml file -----------------#

import xml.etree.ElementTree as et

tree = et.ElementTree(file = 'menu.xml')
root = tree.getroot()
print('root.tag:',root.tag)

for child in root:
	print('tag:', child.tag, 'attributes:', child.attrib)
	for grandchild in child:
		print('\ttag:', grandchild.tag, 'attributes:', grandchild.attrib)


# the number of menu
print('number menu:',len(root))

# the number of breakfast
print('number menu:',len(root[0]))


#----------------- json file -----------------#
#----------------- yaml file -----------------#
#----------------- .ini file -----------------#


