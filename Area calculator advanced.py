# Area calculator addvanced 
# Athor: Zach Hamilton
# Data: 2024/10/30
# Version 1


# This is a code that will calculate diferant shapes area and perimeter or volume perimete. 

# vaild number checker
# This checks whether the numbe that the user inputs is a number that the code can use.
PI = 3.1415926533
def vaild_number(question):
    error_zero_negitive = "Your responce is an invalid number. Try again"
    value_error = "Your responce is an invalid number."
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




print("This is a calculater that find the area and somtimes the perimeter of the shapes")
keep_going = ""                     # "keep_going is the variable that if you changed  will exit the program the while loop."

while keep_going == "":             # This is the main while loop.
    print("Select your shape")      # These print statments tell the user what key to press for each shape.
    print("Press 1 for rectangle")
    print("Press 2 for triangle")
    print("Press 3 for circle")
    
    selection = vaild_number("")    # The variable controls which shape the calculater calculates.

    if selection == 1:
        print("You selected rectangle.")                                    # Lets the user know what shape they chose.

        length = vaild_number("Enter the length of your rectangle.")        # Asks the user to give length of the rectangle. 
        print(f"The length is {length} units.")                             # Give infomation back to the user. 

        height = vaild_number("Enter the width of your rectangle.")         # Asks the user to give width of the rectangle.
        print(f"The height is {height} units.")                             # Give infomation back to the user. 

        rect_perimeter = (length * 2) + (height * 2)                        # Calculates the perimeter of the rectangle.
        area =  length * height                                             # Calculates the area of the rectangle.

        print (f"Perimeter = {rect_perimeter} units.")                      # Tell the user the perimeter of the rectangle.
        print (f"Area = {area} units squared.")                             # Tell the user the area of the rectangle.
       
        keep_going = input("Press enter to calculate another area. Else type any other key to stop.")       # Lets the user break from the loop.

    elif selection == 2:                                                                                    
        print ("The selected triangle.")                                                                    # Lets the user know what shape they chose.
        
        tri_base_length = vaild_number("What is the length of the base of your triangle.")                  # Asks the user for the length of the base of the triangle.
        print (f"The height is {tri_base_length} units)")                                                   # Give infomation back to the user.

        Tri_heigth = vaild_number("What is the height of your tirangle.")                                   # Asks the user for the height of the triangle.
        print(f"The height is {Tri_heigth} units.")                                                         # Give infomation back to the user.

        Tri_area = (Tri_heigth * tri_base_length)/2                                                         # Calculates the area of the triangle

        print(f"Area = {Tri_area} units squared.")                                                          # Tell the user the area of the triangle
        keep_going = input("Press enter to calculate another area. Else type any other key to stop.")       # Lets the user break from the loop.

    elif selection == 3:                                                                                    # This elif does bacily the same as the last too just for the circle. 
        cir_radius  = vaild_number("What is the radius of the circle.")
        print(f"The radius of your circle is {cir_radius} units.")                           
        
        cir_area = (cir_radius* PI)**2                                                                      
        cir_perimeter = 2 * PI * cir_radius                                                                 
        print(f"Area = {cir_area} units squared.")                                       
        print(f"Circumference = {cir_perimeter} units.")                                 
        keep_going = input("Press enter to calculate another area. Else type any other key to stop.")       

    else:                                                                                                   
        print("Your responce is an invalid input. Try again.")                                              # If the user gets to the else something went wrong and it allow them to try again. 

    







    
    


