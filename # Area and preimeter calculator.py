# Area and preimeter calculator 
# Athor: Zach Hamilton
# Data: 2024/10/25
# Version 1



# This checks whether the length/ width that the user inputs is a valid input. If its not then it will ask them to try again. 
def vaild_number(question):
    error_zero_negitive = "Your responce is an invalid number. Length can't be 0 or negitive"
    value_error = "Your responce is an invalid number."
    while True:
        try:
            response = float(input(question))
            if response >= 0:
                break
            else: 
                print(error_zero_negitive)
        except ValueError:
            print(value_error)
    return response
    

# The Keep_going variable allow you to break out of the loop.
print("This is a program that calcuates the area and perimeter of a rectangle.")
keep_going = ""
while keep_going == "":
    length = vaild_number("Enter the length") # Asks user for length of there rectangle. 
    print(f"Your length is {length}")

    width = vaild_number("Enter the width") # Asks user for width of there rectangle. 
    print(f"Your length is {width}")

    perimeter = (length * 2) + (width * 2) #calculates perimeter and area of the rectangle 
    area =  length * width

    print (f"The perimeter of your shape is {perimeter} units") # Tells the user the perimeter and area of the rectangle. 
    print (f"The area of your shape is {area} units")
    
    keep_going = input("Press enter to go again or press any other key to stop. ") # Makes the user able to break out of the loop. 



 




