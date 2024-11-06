# Fence Cost Calculater. 
# Author: Zach Hamilton
# Date: 2024/11/6
# Virsion 2


# defs for the code. The first is for floats and the second is for int. 
def vaild_number(question): 
    error_zero_negitive = "\nYour responce is an invalid number."
    value_error = "\nYour responce is an invalid number."
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

def vaild_int(question):
    error_zero_negitive = "Your responce is an invalid number."
    value_error = "Your responce is an invalid number."
    while True:
        try:
            response = int(input(question))
            if response >= 0:
                break
            else: 
                print(error_zero_negitive)
        except ValueError:
            print(value_error)
    return response

print("\nThis is a program that will calculate the cost of a rectangular fence.")                     # Tell the user what the program does
keep_going = ""                                                                                     # Keep_going is the varable that allows the user to break out of the loop
                                                                                                    
while keep_going == "":                                                                             # Starts the while loop. This is the main section of the code. 

    fence_length = vaild_number("\n\nWhat is the length of the fence in meters?\n")                     # Asks the user for the dimention and cost of the fence per meter.
    fence_width = vaild_number("\nWhat is the width of the fence in meters?\n")                       
    fence_cost = vaild_number("\nWhat is the cost of the fence per meter?\n$")
    
    gate_number = vaild_int("\nHow many gates does the fence have?\n")                               # Asks the user how many gates their fence has. If there are zero fences the code will skip the rest of the gate question. 
    
    if  gate_number > 0:                                                                            # If the number of gates that are in bigger than zero than it will go through this if statement. 
        gate_cost = vaild_number("\nHow much does your gate cost?\n$")                                # Asks the user for the cost and length of the fence. 
        gate_length = vaild_number("\nWhat is the length of the gate(s)? \n")                             

        

        fence_perimeter_gate = (fence_length * 2) + (fence_width * 2) - (gate_number * gate_length) # Calculates the perimeter of the fence not including the length that the gates would take up.
        fence_total_cost_gate = (fence_perimeter_gate * fence_cost) + (gate_number * gate_cost)     # Calculates the total cost of the fence + gates.

        fence_perimeter_error = (fence_length * 2) + (fence_width * 2)                              # This code calculates the perimeter before taking gates into account.  
        negitive_area_error = fence_perimeter_error - (gate_number * gate_length)                   # This code calculates if the gates will take up more length than the whole fence.
        
        if negitive_area_error < 0:                                                                 # Gives error message if the length of the gates is bigger then the length of the fence. 
            print("\nYou Have added more gates then the fence length allows.")
            

        else:   
            print (f"\nThe total cost of the fence will be ${fence_total_cost_gate} including the cost of the gates.")         # Tells the user the total cost of the total. 
            keep_going = input("\nWhat you like to go again? If so than press <enter> otheriwse click any other key to stop.") # Asks the user if they would like to loop. 
            print("___________________________________________________________________________________________")
    
    else:                                                                                                                    # This is the code that doesn't give the user questions about the gates. 
        fence_perimeter_nogate = (fence_length * 2) + (fence_width * 2)                                                      # Finds the perimeter of the fence.
        fence_total_cost_nogate = (fence_perimeter_nogate * fence_cost)                                                      # Finds the cost of the fence not including the gates. 

        print(f"The total cost of your fence is ${fence_total_cost_nogate}.")                                                # Tells the user the total fence cost. 
        keep_going = input("What you like to go again? If so than press <enter> otheriwse click any other key to stop.")    # Asks the user if they want the code go again. 
        print("___________________________________________________________________________________________")