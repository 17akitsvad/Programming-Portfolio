#simple cookie program
def has_cookie():
	try:
	

def set_cookie(name, email):
	cookie = open("zcookie.txt", "w")
	cookie.write(name+"\n")
	cookie.write(email+"\n")
	cookie.close()

def main():
	if has_cookie():
		greet()
	else:
		print "Welcome!"
	name, email = show_instructions()
	set_cookie(name, email)
	
	print("Thank you %s, have a nice day." %s(name)
	
set_cookie("bob", "bob@bob.com")