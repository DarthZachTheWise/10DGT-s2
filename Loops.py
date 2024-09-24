# Loops and indents 
# Author: Zach Hamilton 
# Date: 25/09/2024
# Version 2
# TODO:
    # Get user input (ask user for their name).
    # ask the user for two numbers 
    # Add the numbers togther.  

# Ask the user for their name.
name = input("What is your name?")
print(f"Kia ora {name}.") 

# Ask the user for 2 numbers
num_1 = int(input("What is your favourite number?"))
num_2 = int(input("What is your least favourite number"))

# Add numbers together
sum = num_1 + num_2 
print(f"Your numbers added togther they equal {sum}?")

# for loops. Repeat for a set number of times.
# for starts the loop 
# next is the name of the loop
# in range tells the loop how many times to run
# the number in the () is how many time it repeats
for name_of_loop in range(5):
    print("ha, ")

# while loops run until a codition is met. 
keep_going = "Again" # empty variable
while keep_going == "Again":
    print("looping")
    print("still looping")
    keep_going = ""
    keep_going = input("Type 'again' if you want the computer to laugh again")










