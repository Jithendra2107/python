#1)
#Write a program that asks the user to guess a random integer between 1 and 100.
#Use the random module, and provide feedback like "Too high" or "Too low" until they guess correctly.

"""
import random
import sys

x = random.randint(1,100)
counter = 0

while True:
    try:
        y = int(input("Guess a random integer between 1 and 100: "))
        counter += 1
    except ValueError:
        print("Invalid Input!! Please Enter Integer.")
        continue

    if y >= 1 and y <= 100:
        if y > x:
            print("Too high")
        elif y < x:
            print("Too low")
        else:
            print(f"Guessed Perfect!! It took you {counter} tires.")
            break
    else:
        print("Invalid Number!!! Retry.")
"""

#2
#Create a calculator program (calc.py) that accepts two numbers and an operator (e.g., python calc.py 1 + 2) via the command line.
#Use sys.argv to capture the inputs and sys.exit to handle cases where the user provides the wrong number of arguments.

""" Run the program in the form of [ python day-5.py 20 "*" 20 ] """

import sys

#print(len(sys.argv)) 

if len(sys.argv) == 4:

    try:
        x = int(sys.argv[1])
        y = int(sys.argv[3])
    except ValueError:
        print("Invalid arguments!")
        sys.exit()

    if sys.argv[2] == "+":
        print(x + y)
    elif sys.argv[2] == "-":
        print(x - y)
    elif sys.argv[2] == "*":
        print(x * y)
    elif sys.argv[2] == "/":
        print(x / y)
    else:
        print("Invalid operater!")
        sys.exit()
else:
    print("Wrong number of arguments!")