class A:
	attr = 1
class B(A):
	pass
class C(A):
	attr = 2
class D(B,C):
	pass
class E(B,C):
	attr = C.attr
if __name__ == '__main__':
	x= D()
	print(x.attr)
	y= E()
	print(y.attr)


