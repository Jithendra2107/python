#Even/Odd Identifier: Prompt the user for an integer and print "Even" or "Odd"

"""
value = int(input("What is the Number: "))

if value == 0:
    print("It is Zero!!")
elif value % 2 == 0:
    print("Number is Even!!")
else:
    print("Number is Odd!!")
"""
    
#Positive/Negative Checker: Prompt the user for a number and print if it is positive, negative, or zero.

"""
number = int(input("Enter Number: "))

if number > 0:
    print("Number is Positive!!")
elif number < 0:
    print("Number is Negative!!")
else:
    print("Number is Zero!!")
"""

#Largest of Two: Ask the user for two numbers and print the larger one.

"""
A = int(input("Enter A: "))
B = int(input("Enter B: "))

if A > B:
    print("A is Greater than B")
elif A < B:
    print("B is Greater than A")
else:
    print("A is Equal to B")
"""

#Voting Age: Ask for the user's age. If they are 18 or older, print "Eligible to vote," otherwise print how many years they have left until they turn 18.

"""
age = int(input("Enter Age: "))

if age >= 18:
    print("Eligible to vote!!")
else:
    minor = 18 - age
    print(f"{minor} years left to turn 18!!")
"""

#FizzBuzz Logic: For a number from 1 to 20, print "Fizz" if divisible by 3, "Buzz" if divisible by 5, and "FizzBuzz" if divisible by both.

"""
number = int(input("Enter Number form 1 to 20: "))

if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)
"""

#Season Identifier: Ask the user for a month (1-12) and print the season (Winter, Spring, Summer, or Fall).

"""
month = int(input("Enter the Month Number: "))

if month == 12 or month == 1 or month == 2:
    print("❄️ Winter")
elif month == 3 or month == 4 or month == 5:
    print("🌸 Spring")
elif month == 6 or month == 7 or month == 8:
    print("☀️ Summer")
else:
    print("🍂 Fall/Autumn")
"""

#Simple Calculator: Ask the user for two numbers and an operator (+, -, *, /). Perform the operation and print the result.

"""
x = int(input("Enter X: "))
y = int(input("Enter Y: "))

operator = input("Enter the operation (+,-,*,/): ")

match operator:
    case "+":
        sum = x + y
        print("The Sum of X and Y is:", sum)
    case "-":
        sum = x -y 
        print("The Subtration of X and Y is:", sum)
    case "*":
        sum = x * y 
        print("The multiplication of X and Y is:", sum)
    case "/":
        sum = x / y 
        print("The Divison of X/Y is:", sum)
    case _:
        print("Invalid Operator!!!")
"""

#Leap Year Checker: Write a program that determines if a user-input year is a leap year (a year is a leap year if divisible by 4, but not by 100 unless also divisible by 400).

"""
year = int(input("Enter year: "))

if year % 400 == 0:
    print(f"{year} is a Leap Year!")
elif year % 100 == 0:
    print(f"{year} is not a Leap Year!")
elif year % 4 == 0:
    print(f"{year} is a Leap Year!")
else:
    print(f"{year} is not a Leap Year!")
"""