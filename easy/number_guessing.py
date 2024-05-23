import random

max_range = input("type a number: ")
guesses_nbr = 0

if max_range.isdigit():
	max_range = int(max_range)
	if max_range <= 0:
		print("please type a number larger than 0.")
		quit()
else:
	print("please type a number")
	quit()

random_nbr = random.randint(0, max_range)

while True:
	guesses_nbr += 1
	guess_nbr = input("guess the number: ")
	if guess_nbr.isdigit():
		guess_nbr = int(guess_nbr)
	else:
		print("enter the a number next time.")
		continue

	if guess_nbr == random_nbr:
		print("You Got It Right!!")
		break
	else:
		if guess_nbr > random_nbr:
			print("You gessed above the number!")
		else:
			print("You gessed less than the number!") 
print("You Got It in", guesses_nbr, "guesses")