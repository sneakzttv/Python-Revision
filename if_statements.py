# If statements
temperature = 35

# : indicates a block of code similar to {} in other languages
# removing the indent closes the function
if (temperature > 30):
    print("It's a hot day")
    print("Drink plenty of water")
elif (temperature > 20):
    print("It's a nice day")
elif (temperature > 10):
    print("It's a bit cold")
else:
    print("It's cold")

print("Done")