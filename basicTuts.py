print("\nWelcome to my simple Odd or Even app!")

num = int(input("What number are you thinking? (-1 to exit the program) : "))
x = True

while x == True:
	result = num % 2
	if num == -1:
		x = False
		result = None
	
	if result == 0:
		print(str(num) + " is an Even number!")
	elif result == 1:
		print(str(num) + " is an Odd number!")
	
	if result != None:
		num = int(input("Have another? : "))