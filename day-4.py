#1
"""Write a script that prompts the user for an integer using input(). 
Wrap the conversion int(input(...)) in a try...except block to catch a ValueError 
and print the message "That is not an integer."""

"""
try:
    x = int(input("Enter an integer: "))
    print(f"X is {x}")

except ValueError:
    print("That is not a integer!")
"""

#2
"""Refactor your previous code to use the else block with try...except.
Ensure that you only print the user's input (e.g., "x is {x}")
if the conversion successfully completed without triggering an exception."""

"""
try: 
    x = int(input("Enter an integer: "))
except ValueError:
    print("This is not an Integer!")
else:
    print(f"X is {x}")
"""

#3
"""Combine a while True loop with try...except to continuously prompt the user
for an integer until they provide a valid one. 
Use the break keyword to exit the loop only upon a successful conversion."""

"""
while True:
    try:
        x = int(input("Enter Integer: "))
        break
    except ValueError:
        print("This is not a integer!")

print(f"x is {x}")    
"""

#4
"""Modify your reprompting loop to use the pass keyword inside the except block.
Observe how the program behaves silently instead of printing an error message when the user provides invalid input."""\

"""
while True:
    try:
        x = int(input("Enter Integer: "))
        break
    except ValueError:
        pass

print(f"X is {x}")
"""

#5
"""Create a reusable function named get_int that accepts a prompt string as an argument. 
The function should perform the while True validation loop and
return the final valid integer value to the caller."""

"""
def main():
    x = get_int()
    print("X is the Integer: ", x)

def get_int():
    while True:
        try:
            return int(input("Enter Integer: "))
        except ValueError:
            pass

main()
"""        

#6
""" Create a main() function. 
Inside main(), use your get_int function to prompt the user for two different variables,
"x" and "y". Once you have both values, print their sum. 
Ensure your program handles invalid inputs for both prompts gracefully without crashing."""


def main():
    x = get_int("Enter X: ")
    y = get_int("Enter Y: ")
    print("X + Y is:", x+y)

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter the Integer!")
    
main()
        
