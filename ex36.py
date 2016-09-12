sign = "> "

def enter():
	print "Welcome to the magic tower!"
	print "Only get to the End Chamber, you can escape."
	print "Or, you will be trapped in forever! Good luck."
	print "Please choose first, or second floor:"
	
	choice = raw_input(sign)
	
	if choice == "first":
		firstFloor()
	elif choice == "second":
		secondFloor()
	else:
		die("I said first or second floor!")


#------------------------Floors------------------------

def firstFloor():
	print "Hohoho~ welcome to first floor!"
	print "Now, you have two choice, chamber1 or chamber2"
	print "Which do you prefer? (enter 1 or 2)"
	
	choice = raw_input(sign)
	
	if int(choice) == 1:
		firstFloorChamber1()
	elif int(choice) == 2:
		firstFloorChamber2()
	else:
		die("Stupid human... I said \"enter 1 or 2\"!")

		
def secondFloor():
	print "Well, well~ you come to the second floor!"
	print "You have two choice now, chamber1 or chamber2"
	print "Which do you prefer? (enter 1 or 2)"
	
	choice = raw_input(sign)
	
	if int(choice) == 1:
		secondFloorChamber1()
	elif int(choice) == 2:
		secondFloorChamber2()
	else:
		die("Oh dear, how dare you... I said \"enter 1 or 2\"!")

		
def thirdFloor():
	print "That's excting, finally someone get to the third floor!"
	print "You also have two choice, chamber1 or chamber2"
	print "Which do you prefer? (enter 1 or 2)"
	
	choice = raw_input(sign)
	
	if int(choice) == 1:
		thirdFloorChamber1()
	elif int(choice) == 2:
		thirdFloorChamber2()
	else:
		die("What a pity, you were so close to the End Chamber...")
		
		
#-----------------------------------Chambers--------------------------------------
		
def firstFloorChamber1():
	print "It's Chamber1,you will be transfered to the second floor."
	print "Transfering... ... ..."
	secondFloor()

	
def firstFloorChamber2():
	print "It's Chamber2, you will be transfered to the third floor."
	print "Transfering... ... ..."
	thirdFloor()
	
	
def secondFloorChamber1():
	print "It's Chamber1, you will be transfered to the first floor."
	print "Transfering... ... ..."
	firstFloor()
	
	
def secondFloorChamber2():
	print "It's Chamber2, you will be transfered to the first floor."
	print "Transfering... ... ..."
	firstFloor()
	
	
def thirdFloorChamber1():
	print "It's Chamber1, congratulations!"
	print "The End Chamber just in front of you, push the door:"
	
	choice = raw_input(sign)
	
	if choice == "push":
		endChamber()
	else:
		die("I meant PUSH! PUSH! PUSH! Damn...")
		
		
def thirdFloorChamber2():
	print "It's Chamber2, you will be transfered to the second floor."
	print "Transfering... ... ..."
	secondFloor()

def endChamber():
	print "Wow, it's the End Chamber, you are free to go"
	print "Enjoy the fantastic world~"
	
	exit(0)
	
def die(reason):
	print reason
	print "You die. Game over."
	exit(0)

# start the game
enter()