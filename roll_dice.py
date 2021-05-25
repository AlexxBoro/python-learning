import random

roll = random.randint(1, 6)

guess = int(input("guess the dice roll:\n"))

if guess == roll:
    print("correct! -> " + str(roll))
else:
    print("not correct -> " + str(roll))
