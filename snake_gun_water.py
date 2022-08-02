import random

n = int(input('Enter number of rounds: '))

# Snake(s), Water(w), Gun(g)
options = ['s', 'w', 'g']

# Round numbers
rounds = 1

# Count of computer wins
computer_win = 0

# Count of player wins
user_win = 0

# For n rounds of game
while rounds <= n:

	# Display round
	print(f"Round :{rounds}\nSnake - 's'\nWater - 'w'\nGun - 'g'")

	# Exception handling
	try:
		player = input("Choose your option: ")
	except EOFError as e:
		print(e)

	# Control of bad inputs
	if player != 's' and player != 'w' and player != 'g':
		print("Invalid input, try again")
		continue

	# random.choice() will randomly choose
	computer = random.choice(options)

	# Conditions based on the game rule
	if computer == 's':
		if player == 'w':
			computer_win += 1
		elif player == 'g':
			user_win += 1

	elif computer == 'w':
		if player == 'g':
			computer_win += 1
		elif player == 's':
			user_win += 1

	elif computer == 'g':
		if player == 's':
			computer_win += 1
		elif player == 'w':
			user_win += 1

	# Announce winner of every round
	if user_win > computer_win:
		print(f"You Won round {rounds}")
	elif computer_win > user_win:
		print(f"Computer Won round {rounds}")
	else:
		print("Draw!!")

	rounds += 1

# Final winner based on the number of wons
if user_win > computer_win:
	print("Congratulations! You Won")
elif computer_win > user_win:
	print("You lose!!")
else:
	print("Match Draw!!")