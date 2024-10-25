# Error check 
# Author: Zach Hamilton
# Date: 2024/10/25
# Version 3


# Code that tests that a valid number is entered (V1)
'''done = False # This is a Boolean. It is a switch.
while not done: # while loop that runs until a validi number is entered. 
    num_1 =int(input("Please enter your value"))
    
    done = True

print(f"The number you entered is {num_1}.")'''


# Code that tests that a valid number is entered (V2)
# Create a function to call every tim e I ask the user to a number. 
# A function is a chunk of code that does somthing. A can use a function over and over. To use a function, I 'call' it by writing the name.

'''def test_int_num(question):
    done = False
    while not done:
    # The 'question is a place holder. 
        try:
            num = int(input(question)) # this tries for a valid input
            done = True
        except ValueError:
            print("That is not a valid number. Try again")
        
    return(num) # Gives us back the value of num  so that i can use it outside the function. 


# Main program 
num_1 = test_int_num("Please enter your first number:")
print(f"You enteed {num_1}.")

num_2 = test_int_num ("Please enter your second number:")
print(f"You enteed {num_2}.")

num_3 = test_int_num ("Please enter your third number:")
print(f"You enteed {num_3}.")

sum = num_1 + num_2 + num_3

print(f"The Sum of {num_1}, {num_2} and {num_3} = {sum}. ")'''

# Version 3. Refining my code. Making it more pythonic 
# Ask the user to picj a number is a range.

def valid_num(question, low, high):
    error_message = f"That is not a valid number. Please enter a interger between {low} and {high}. :-("
    while True: 
        try:
            response = int(input(question))
            if low <= response <= high:
                break
            else:
                print(error_message)
        except ValueError:
            print(error_message)
    return response # make the value stored in the response varable availabel outside the loop 
    


num_1 = valid_num(f"Enter a nmber between 1 and 15 :", 1, 15)
print(f" You entered {num_1}")
 
num_2 = valid_num("Know enter a number between 50 and 100", 50, 100)
print(f" You entered {num_2}")

num_3 = valid_num("Know enter a number between 70 and 80", 70, 80)
print(f"You entered {num_3}")

# Mulitly the numbers

product = num_1 * num_2 * num_3
print(f"The product of your three numbers is {product}.")




