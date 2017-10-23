items = ["aaa", 111, (4,5), 2.01]
tests = [(4,5), 3.14]

for key in tests:
	for item in items:
		if item == key:
			print(key, "was found")
			break
	else:
		print(key, "not found!")

