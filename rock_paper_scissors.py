from random import randint

my_win = 0
my_loss = 0
my_tie = 0

#creat a list of play options
t = ["Rock", "Paper", "Scissors"]

#Random function: Assigns a random play
computer  = t[randint(0,2)]

#set player to False
start_game = False
while start_game == False:
	start_game = input("Hey! Want to Play a Game? (yes/no):")
	if start_game.lower () != "yes": 
		break
player = False
while player == False:
#Sets the player to True
	player = input("Rock, Paper, Scissors? ")
	if player == computer:
		print("Tie")
		my_tie += 1
	elif player == "Rock":
		if computer == "Paper":
			print("You lose :(", computer, "covers", player)
			my_loss += 1 
		else:
			print("You win :D!", player, "crushes", computer)
			my_win += 1 
	elif player == "Paper":
		if computer == "Scissors":
			print("You lose :(", computer, "slices", player)
			my_loss += 1  
		else:
			print("You win :D!", player, "covers", computer) 
			my_win += 1 
	elif player == "Scissors":
		if computer == "Rock":
			print("You lose :(", computer, "crushes", player)
			my_loss += 1 
		else:
			print("You win :D !", player, "slices", computer)
			my_win += 1 
		#valid function - check the validity of the answer
	else:
		print("Invalid answer! Please check your spelling again :)")

	print ("Your wins: %d" % my_win)
	print ("Your loses: %d" % my_loss)
	print ("Your ties: %d" % my_tie)

	play_again = input("Want to Play Again? (yes/no):")
	if play_again.lower () != "yes": 
		break

	

	#loop player by setting it to false
	player = False
	computer = t[randint(0,2)]




