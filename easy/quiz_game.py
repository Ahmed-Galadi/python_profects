print("Welcome to THE QUIZ GAME!")

playing = input("Do You Wanna Play? ")

if playing.lower() != "yes":
	quit()

print("OKAY! let's play!")

score = 0

answer = input("What CPU stands for? ")

if answer.lower() == "central processing unit":
	print("CORRECT! U R doing GREAT!!")
	score += 1
else:
	print("Wrong Answer :(")

answer = input("What RAM stands for? ")

if answer.lower() == "random access memory":
	print("CORRECT! U R doing GREAT!!")
	score += 1
else:
	print("Wrong Answer :(")

answer = input("What GPU stands for? ")

if answer.lower() == "graphics processing unit":
	print("CORRECT! U R doing GREAT!!")
	score += 1
else:
	print("Wrong Answer :(")

answer = input("What ROM stands for? ")

if answer.lower() == "read only memory":
	print("CORRECT! U R doing GREAT!!")
	score += 1

else:
	print("Wrong Answer :(")

print("<< you got " + str((score / 4) * 100) + "%.")