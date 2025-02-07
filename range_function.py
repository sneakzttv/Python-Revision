# Range functions

# returns range object, can store a sequence of numbers
range(5)

# returns object structure (0, 5)
numbers = range(5)
print(numbers)

# for loop
for number in numbers:
    print(number)

# specific range i.e 5-10 (excludes last)
numbers = range(5, 10)
for number in numbers:
    print(number)

# using 3rd parameter, step (skips every 2nd)
numbers = range(5, 10, 2)
for number in numbers:
    print(number)

# shorthand
for number in range(5):
    print(number)