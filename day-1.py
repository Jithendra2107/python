# Practise On Strings
"""
name = input("What is your name? ")
name = name.strip().title()
print("Hello,", name)
"""

"""
name = input("What is your name? ")
print("Hello,", name, end=", ")
print("Welcome to the World of Wizards!!")
reply = input("Reply? ")
print("Your Room no is: 402!! Have a nice Day")
"""

"""
name = input("What is your name? ")
print(f"Hello, {name} Welcome to World of Wizards")
"""

# Practise on INTegers & Folat
"""
print("Welcome to the World of Addition!!!!")
x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))
print("The addition of two no's is:",x + y)
"""

"""
print("Welcome to the World of Addition!!!!")
x = float(input("Enter First Number: "))
y = float(input("Enter Second Number: "))
z = round(x+y)
print(f"The addition of two no's is: {z:.2f}")
"""

"""
Number = int(input("Enter the Base Number: "))
Exponent = int(input("Enter the Exponent: "))
Answer = Number**Exponent
print(Answer)
"""

"""
Divident = int(input("Enter the Divident: "))
Divisor = int(input("Enter the Divisor: "))
Reminder = Divident % Divisor
print(f"The reminder is {Reminder}")

"""


def greet(name="world!"):
    print(f"Hello, {name}")

#greet()
greet(input("Enter Your Name: "))


"""
def add(a,b):
    return a+b

x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))
print("Additon is:",add(x,y))
"""
"""
def main():
    name = input("What is your name: ")
    f_name = format(name)
    print_n = print_name(f_name)

def format(name):
    return name.strip().title()

def print_name(f_name):
    print(f"Hello {f_name}!!")

main()
"""