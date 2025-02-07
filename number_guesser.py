import random

# Ignore the upper value in the range 1 - 9
# 1 number is 0 to number random.randrange(10) is the same etc
print(random.randrange(0, 10))

# int incldues the upper value
print(random.randint(0, 10))

top_of_range = input("Type a number: ")

if (top_of_range.isdigit()):
    top_of_range = int(top_of_range)

    if (top_of_range <= 0):
        print("Please type a number larger than 0 next time")
        quit()
else:
    print("Please type a number next time")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0
print(random_number)

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if (user_guess.isdigit()):
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue

    if (user_guess == random_number):
        print("You got it!")
        break
    elif (user_guess > random_number):
            print("above the number")
    else:
        print("below the number")

print("You got it in", guesses, "guesses")