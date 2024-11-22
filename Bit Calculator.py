# Bit Calculator
# Author: Zach Hamilton
# Date: 2024/11/13
# Virsion 1 


# This program will check if that what you entered would give an error. If it does than it will tell you what you got wrong and repeat the question. 
def valid_number(question):
    error = "\nPlease enter a intager"
    error_less_0 = "\nplease enter a number larger than 0"
    while True:
        try:
            responce = int(input(question))
            if responce > 0:
                break 
            else:
                print(error_less_0)
        except ValueError:
            print(error)
    return responce

#Title
print("\nThis is a program that will tell you the number of bits  interagers, text or a image use.\n")

# This is a while loop that will keep going until the user ends the program. 
keep_going = ""
while keep_going == "":
    # Lets the user pick which program calculator they want to pick.
    selection = valid_number("\nSelect what type of data you would like to calculate.\n\nPress 1 for text\nPress 2 for integers\nPress 3 for image\n")

    
    if selection == 1:
        
        # This if statment tells the user to input text and it will calculate the amount of bits in the text by counting the amount of charictor and timeing them by 8. 
        
        text_bit = len(input("\nWrite in the text that you want to calculate the number of bits that it uses.\nThe calculation will only be accurate if you use ascii charictors\n"))* 8
        print(f"\nThe number of bits that are in the text are {text_bit}")
        keep_going = input("\nIf you would like to do another calculation press <enter>. If not press any other key.")

    
    elif selection == 2:
        # This if statment tells the user to enter a number and it calculates the amount of bits in the number by turning it into binary and counting the amount of charictors in the binary.
        intager_bit  = len(str(bin(valid_number("\nEnter the intager that you would like to calculate the number of bits that it uses.\n" ))[2:]))
        print(f"The number of bits in the intager is {intager_bit}")
        keep_going = input("\nIf you would like to do another calculation press <enter>. If not press any other key.")
    # This stament tells the uesr to enter the width and height of a image in pixel, finds the number of pixels in the whole image and then times them by 24 to find the number of bits is the image. 
    elif selection == 3:

        print("\nThis calculator assumes that your image has 24 bit pixels")
        hight = valid_number("\nWhat is the height of your image in pixels\n")
        width = valid_number("\nWhat is the width of your image in pixels\n")
        image_bit = hight * width * 24
        print(f"\nThe number of bits in the image is {image_bit}")

        keep_going = input("\nIf you would like to do another calculation press <enter>. If not press any other key.")
    # Goes to this if the user doesn't put in a valid input for selection
    else:
        print("\nPLease enter either 1, 2, or 3")

    print("Thank you for using this bit calculator")
    

print("Thank you for using this bit calculator.")




intager_bit  = len(str(bin(valid_number("\nEnter the intager that you would like to calculate the number of bits that it uses.\n" ))[2:]))