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
	
def positive(a):
	return a > 0

def bigger(a, b):
	return a > b

def at_least_13(a):
	return a >= 13
	
def at_most_13(a):
	return a <= 13
	
def biggest(a, b):
	if a > b:
		return a
	elif b > a:
		return b
	else:
		return "They're the same"

def smallest(a, b):
	if a < b:
		return a
	elif b < a:
		return b
	else:
		return "They're the same"	
		
def letter_grade(a):
	if a < 60:
		return "F"
	elif a < 70:
		return "D"
	elif a < 80:
		return "C"
	elif a < 90:
		return "B"
	elif a >= 90 < 101:
		return "A"
	elif a > 100:
		return "A++"
		
def food_tax(subtotal, type):


def big3reorder(a, b, c):
	list = [a, b, c]
	list[a] = 
	
def hello():
	return "Hello"

def nothing():
	return ""
	
def second_letter(two):
	return two[1]
	
def sliceOfPerfection(str, n1, n2):
	return str[n1:n1+n2]

def short_list():
	return [1, 2, 3]
	
def main_strings():
	print "testing nothing(): " , nothing()
	print "testing hello(): " , hello()
	print "testing second_letter('cheese'): " , nothing("cheese")
	print "testing sliceOfPerfection(tacobell): ", sliceOfPerfection("trees tacobell moosetracks", 7, 6)
	
	
	
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
	

def main_boolean():
	print "testing positive(34): ", positive(34)
	print "testing xsame(true, true): ", xsame(True, True)
	print "testing xsame(true, false): ", xsame(True, False)
	print "testing xsame(false, true): ", xsame(False, True)
	print "testing xsame(false, false): ", xsame(False, False)	
	print "testing bigger(34, 24): ", bigger(34, 24)
	print "testing at least 13(13): ", at_least_13(13)
	print "testing at most 13(13): ", at_most_13(13)
	
	
	
def main_lists():
	print "testing short list(): ", short_list()
	
def main_conditional():
	

def main():
	main_function()
	main_arithmetic()
	
main()