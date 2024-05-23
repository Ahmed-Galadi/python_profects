print("Welcome to THE QUIZ GAME!")

playing = input("Do You Wanna Play? ")

if playing != "yes":
	quit()

print("OKAY! let's play!")

answer = input("What CPU stands for? ")

if answer == "central processing unit":
	print("CORRECT! U R doing GREAT!!")
else:
	print("Wrong Answer :(")
	quit()

answer = input("What RAM stands for? ")

if answer == "random access memory":
	print("CORRECT! U R doing GREAT!!")
else:
	print("Wrong Answer :(")
	quit()

answer = input("What GPU stands for? ")

if answer == "graphics processing unit":
	print("CORRECT! U R doing GREAT!!")
else:
	print("Wrong Answer :(")
	quit()

answer = input("What ROM stands for? ")

if answer == "read only memory":
	print("CORRECT! U R doing GREAT!!")
	print("CONGRATULATIONS!! U WON :D")
else:
	print("Wrong Answer :(")
	quit()