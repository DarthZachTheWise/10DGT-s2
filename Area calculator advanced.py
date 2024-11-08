# Area calculator addvanced 
# Athor: Zach Hamilton
# Data: 2024/10/30
# Version 3


# This is a code that will calculate diferant shapes area and perimeter or volume perimete. 

# vaild number checker
# This checks whether the numbe that the user inputs is a number that the code can use.
PI = 3.1415926533
def vaild_number(question):
    error_zero_negitive = "\nYour responce is an invalid number. Try again.\n"
    value_error = "\nYour responce is an invalid number.\n"
    while True:
        try:
            response = float(input(question))
            if response > 0:
                break
            else: 
                print(error_zero_negitive)
        except ValueError:
            print(value_error)
    return response




print("\nThis is a calculater that find the area and sometimes the perimeter of the shapes")
keep_going = ""                     # "keep_going is the variable that if you changed  will exit the program the while loop."

while keep_going == "":             # This is the main while loop.
                
    selection = vaild_number("\nSelect your shape\n\nPress 1 for rectangle\nPress 2 for triangle\nPress 3 for circle\n")    # These print statments tell the user what key to press for each shape. The variable controls which shape the calculater calculates.

    if selection == 1:
        print("\nYou selected rectangle.\n")                                    # Lets the user know what shape they chose.

        length = vaild_number("\nWhat is the length of your rectangle?\n")    # Asks the user to give length of the rectangle. 
         
        height = vaild_number("\nWhat is the width of your rectangle?\n")     # Asks the user to give width of the rectangle.
        
        rect_perimeter = (length * 2) + (height * 2)                          # Calculates the perimeter of the rectangle.
        area =  length * height                                               # Calculates the area of the rectangle.

        print (f"\nPerimeter = {rect_perimeter} units.")                      # Tell the user the perimeter of the rectangle.
        print (f"\nArea = {area} units squared.")                             # Tell the user the area of the rectangle.
       
        keep_going = input("\n\nPress enter to calculate another area. Else type any other key to stop.")       # Lets the user break from the loop.

    elif selection == 2:                                                                                    
        print ("\nYou selected triangle.\n")                                                                    # Lets the user know what shape they chose.
        
        tri_base_length = vaild_number("\nWhat is the length of the base of your triangle?\n")                # Asks the user for the length of the base of the triangle.
       
        Tri_heigth = vaild_number("\nWhat is the height of your tirangle?\n")                                 # Asks the user for the height of the triangle.
        
        Tri_area = (Tri_heigth * tri_base_length)/2                                                           # Calculates the area of the triangle

        print(f"\nArea = {Tri_area} units squared.")                                                          # Tell the user the area of the triangle
        keep_going = input("\n\nPress enter to calculate another area. Else type any other key to stop.")       # Lets the user break from the loop.

    elif selection == 3:   
        print("\nYou selected circle.\n")                                                                       # This elif does bacily the same as the last two just for the circle. 
        cir_radius  = vaild_number("\nWhat is the radius of the circle?\n")
                                   
        
        cir_area = (cir_radius* PI)**2                                                                      
        cir_perimeter = 2 * PI * cir_radius

        print(f"\nArea = {cir_area} units squared.")                                       
        print(f"\nCircumference = {cir_perimeter} units.")  
                                       
        keep_going = input("\n\nPress enter to calculate another area. Else type any other key to stop.")       

    else:                                                                                                   
        print("\nYour responce is an invalid input. Try again.")                                              # If the user gets to the else something went wrong and it allow them to try again. 