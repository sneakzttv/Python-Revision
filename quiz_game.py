print("Welcome to my game")

playing = input("Do you want to play? ")

if (playing.lower() != "yes"):
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if (answer.lower() == "central processing unit"):
    score += 1
    print("Correct")
else:
    print("Incorrect")

answer = input("What does GPU stand for? ")
if (answer.lower() == "graphics processing unit"):
    score += 1
    print("Correct")
else:
    print("Incorrect")
    
answer = input("What does RAM stand for? ")
if (answer.lower() == "random access memory"):
    score += 1
    print("Correct")
else:
    print("Incorrect")

answer = input("What does PSU stand for? ")
if (answer.lower() == "power supply unit"):
    score += 1
    print("Correct")
else:
    print("Incorrect")

print("You got " + str(int((score / 4 * 100))) + "%")