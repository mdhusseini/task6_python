from random import randint

guessList=[]
magicNo = randint(1, 100)
#print("Magic no is "+ str(magicNo))

def isGuessCorrect(guessNum,magicNo):
	if (guessNum > magicNo):
		print ("Oops, Your guess was HIGH.")
	elif (guessNum < magicNo):
		print ("Oops, Your guess was LOW.")
	else:
		print ("Good Job! You guessed it!")
		quit()

for attempts in range(10, 0, -1):
	print("You have "+str(attempts)+" attempts left")
	guessNum = int(input('Guess the number from 1 to 100: '))
	isGuessCorrect(guessNum,magicNo)
	guessList.append(guessNum)
	
print(guessList)
print("Sorry, You dint guess my number. It was "+str(magicNo))



