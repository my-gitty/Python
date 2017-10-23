y = input('Enter a int:')
y = int(y)
x = y // 2
while x > 1 or y != 2:
	if y % x == 0:
		print(y,'has factor',x)
		print('\n')
		break
	x -= 1
else:
	print(y, 'is prime\n')

