import random


def roll(high):
    return random.randint(0, high)

sides = int(input("Enter number of sides on the dice: "))

while True:
    print("Dice Rolled {}!".format(roll(sides)))
    response = input("Roll again?(y/n): ")
    if response.lower() != 'y':
        break
