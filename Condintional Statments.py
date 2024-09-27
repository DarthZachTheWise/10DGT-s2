# Title:Conditional statements and while loops 
# Author: Zach Hamilton 
# Date: 2024-09-27
# Version 1
# TODO: Creare a program that asks a uesr a question.
# and returns a response based an the anxser of the user.


# Main loop. Keeps running until a condition is met. 
keep_going = ""
while keep_going == "":
    # Asking the user for an input to a question. 
    like_coffee = input("Do you like coffee?").lower() # .lower makes the input all lower case
    if like_coffee == "yes" or like_coffee == "y":
        print("I like coffee too!")
    elif like_coffee == "no" or like_coffee == "n":
        print("You're missing out")
        
        like_tea = input("Would you like tea instead?").lower()
        if like_tea == "yes" or like_tea == "y":
            print("Good for you.") 
        elif like_tea == "no" or like_tea == "n":
            print("You're missing out again!")
        else:
            print("I don't understand")
    else:
        print("I don't understand.")
    
    keep_going = input ("Press <enter> to do agains or any other key to quit")


