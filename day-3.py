#Write a program that initializes a variable i to 5 and uses a while loop to print the word "meow" exactly 5 times, decrementing i in each iteration.

"""
i =5
while i > 0:
    print("meow", i)
    i -=1
"""

#Rewrite the previous task using a for loop and the range() function. How does the syntax change?

"""
for n in range(5):
    print("meow", n)
"""

#The following code causes an infinite loop. Identify the issue and provide the corrected version: python i = 1 while i <= 3: print("meow")

    # Their is no statement for regulating the i where the i is constant (i = 1), the get stuck with the condition true.

#Create a list named houses containing "Gryffindor", "Hufflepuff", "Ravenclaw", and "Slytherin". Use a for loop to print each item in the list.

"""
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw","Slytherin"]
print(len(houses))

for i in range(len(houses)):
    print(houses[i])
"""

#Modify your loop to print the index and the value (e.g., 0 Gryffindor). Hint: Consider using range() combined with len().

"""
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw","Slytherin"]

for i in range(len(houses)):
    print(i,houses[i], sep=": ")
"""

""" Create a dictionary named student_houses where keys are student names ("Harry", "Hermione", "Ron") and values are their houses.
 Write a loop that iterates through the dictionary and prints: "[Name] is in [House]". """

"""
student_houses = {
    "Harry": "Gryffindor",
    "Hermione": "Gryffindor",
    "Ron": "Gryffindor",
    "Drako": "Slytherin"
}

for student in student_houses:
    print(student, student_houses[student], sep=": ")
"""

#Write a function get_positive_int() that uses a while True loop and break to repeatedly ask the user for an input until they provide a positive integer, then return that integer.

"""
def main():
    i = get_positive_int()
    print(f"{i} is a Positive integer")

def get_positive_int():
    
    while True:
        i = int(input("Enter Positive integer: "))
        if i > 0:
            return i
        else: 
            continue

main()
"""

#Write a program that accepts an integer n and uses a nested loop to print a right-aligned triangle of hashes. For example, if n=3:

"""
n=3
k=1
f=2
for i in range(n):  
    for j in range(k):
        for z in range(f):
            print(" ", sep="",end="")
        f=f-1
        print("#", sep="", end="")
    print()
    k = k+1
"""
"""
n = 3
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(i):
        print("#",end="")
    print()
    """

# Create a list named roster containing three dictionaries. 
#Each dictionary should have the keys: name, house, and patronus.
#Write a loop that iterates through this list and prints each student's information in a clean, formatted way (e.g., "Name: Harry, House: Gryffindor, Patronus: Stag").

"""
roster = [{"Name": "Harry", "House": "Gryffindor", "Patronus": "Stag"},
          {"Name": "Hermione", "House": "Gryffindor", "Patronus": None},
          {"Name": "Ron", "House": "Gryffindor", "Patronus": None},
          {"Name": "Drako", "House": "Gryffindor", "Patronus": None}
        ]
for student in roster:
   # print('Name: '+student["Name"]+', '+'House: '+student["House"]+', '+'Patronus: '+ str(student["Patronus"]))
    print(f"Name: {student["Name"]}, House: {student["House"]}, Patronus: {student["Patronus"]}")
"""

