# some random integer shit
from random import randint
def rint():
	r = randint(64,90)
	if (r==64):
		r = 42
	return r
	
def main():
	for i in range (65535):
		z = rint()
		print(z,end="")
main()