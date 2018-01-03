import multiprocessing
import os
import time

def do_this(what):
	whoai(what)

def whoai(what):
	print("Process %s says: %s" % (os.getpid(), what))

def loopy(name):
	whoai(name)
	start = 1
	stop = 1000000
	for num in range(start, stop):
		print("\tNumber %s of %s. Honk!" % (num, stop))
		time.sleep(1)


if __name__ == "__main__":
	whoai("I'm the main program")
	for n in range(4):
		p = multiprocessing.Process(
				target = do_this, 
				args = ("I'm function %s" % n,) # attention the comma
				)
		p.start()
	time.sleep(2)
	p.terminate()

	

	print()
	whoai("main")
	p = multiprocessing.Process(target = loopy, 
							args = ("loopy",)) # attention the comma
	p.start()
	time.sleep(5)
	p.terminate()
