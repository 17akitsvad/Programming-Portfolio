import random

def roll_die(sides):
    r = random.randrange(1, sides+1)
    return r

def take_turn(plnum):
	turn_pts = 0
	keep_rolling = 1
	print 	
roll_die(6)
