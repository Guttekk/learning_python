import random

min = 1
max = 100
magicNumber = random.randint(min,max)

message = "Pick a number between {0} and {1}:"
print(message.format(min,max))

found = False

while not found:
    number =  int(input())
    if number == magicNumber:
        found = True
        print("Good guess!")
    elif number < magicNumber:
        print("Guess higher ")
    elif number > magicNumber:
        print("Guess lower ")
