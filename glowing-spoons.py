from os import path
from sys import exit, argv

def run(debug=True):
	print "You have started:\n", 
	print 10*'*', "Glowing Spoons", 10*'*'
	print "A game by Franco Quiroga. \nWritten in python2"
	
	if debug:
		print "Currently, the debug option is Active"

	return

class Character(object):

	def __init__(self):
		pass

print "Hello world!"
run()
