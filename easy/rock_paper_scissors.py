import random

player_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
	user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
	if user_input == "q":
		break
	if user_input not in options:
		continue

	random_nbr = random.randint(0, 2)
	computer_choice = options[random_nbr]
	print("computer picked", computer_choice + ".")

	if user_input == "rock" and computer_choice == "scissors":
		player_wins += 1
		print("You Won!")
	elif user_input == "scissors" and computer_choice == "paper":
		player_wins += 1
		print("You Won!")
	elif user_input == "paper" and computer_choice == "rock":
		player_wins += 1
		print("You Won!")
	else:
		computer_wins += 1
		print("You Lost!!")

print("computer wins:", computer_wins)
print("player wins:", player_wins)
print("Goodbye!!")
