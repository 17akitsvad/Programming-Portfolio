# python learning exercises

# Functions
def echo(thing):
	return thing

def swap(thing1, thing2):
	return thing2, thing1

	
def main_function():
	print "testing echo('marco'): ", echo('marco')
	print "testing echo('shut up'): ", echo('no, you shut up')
	print "testing swap('fame', 'fortune')", swap('fame', 'fortune')


#Arithmetic Functions
def reverse(x):
	return -x

def plus(a, b):
	return a + b
	
def diff(x, y):
	return x - y
	
def abs_diff(d, b):
	diff = d - b
	if diff < 0:
		diff *= -1
	return diff

def devide(a,b):
	return a / float(b)
	
	
def remainder(a, b):
	return a % b
	
	
def power(a, b):
	result = 1
	for i in range(b):
		result *= a
	return result

def calculate(a, b, c, d, e):
	return (a+b / d - e) * c
	
def xsame(b, g):
	return b == g
	
def main_arithmetic():
	print "test reverse(3): ", reverse(3)
	print "test reverse(-3): ", reverse(-3)
	print "testing plus(1, 1): ", plus(1, 1)
	print "testin' diff(12, 5): ", diff(12, 5)
	print "testin' abs_diff(5,10): ", abs_diff(5, 10)
	print "testin' devide(40, 16): ",devide(40, 16)
	print "testin' remainder(100, 30): ", remainder(100, 30)
	print "testin' remainder(2, 3): ", power(2, 3)
	print "calculate(1, 2, 3, 4, 5): ", calculate(1, 2, 3, 4, 5)
	print "xsame(true, true): ", xsame(True, True)
	print "xsame(true, false): ", xsame(True, False)
	print "xsame(false, true): ", xsame(False, True)
	print "xsame(false, false): ", xsame(False, False)
	
	
	

def main():
	main_function()
	main_arithmetic()
	
main()