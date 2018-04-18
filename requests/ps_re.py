import re
code = 'BIT100081'

# search
match = re.search(r'[1-9]\d{5}', code)
if match:
	print(match.group(0))
else:
	print("No re.search")


# match
match = re.match('r[1-9]\d{5}', code)
if match:
	print(match.group(0))
else:
	print("No re.match")


# findall
code += 'TSU100084'
ls = re.findall(r'[1-9]\d{5}', code)
if ls:
	print(ls)
else:
	print("No re.findall")


# split
sp = re.split(r'[1-9]\d{5}', code)
print(sp)

sp = re.split(r'[1-9]\d{5}', code, maxsplit = 1)
print(sp)


# finditer
for m in re.finditer(r'[1-9]\d{5}', code):
	if m:
		print(m.group(0))

#sub
sub = re.sub(r'[1-9]\d{5}', ':zipcode ', code)
print(sub)
