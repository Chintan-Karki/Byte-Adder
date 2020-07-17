# IMPORT all the methods in binAdder module
from binAdder import *

# declaring binary validation method


def binVal():
    # TODO - Print Instructions on binary addition process

    print("NOTE: The binary value must lie in between 00000000 and 11111111.\n")
    loop2 = False
    # starting a loop for first binary number validation
    # Loop is stopped only when the input is valid
    # loop2 is set true when INPUT is valid
    # loop2 runs until it is false
    while(not loop2):
        # take input as string
        bin1 = str(input("Enter a binary number: ").strip())
        # check empty inputs
        if bin1 != '':
            # Converting input to a set for  checking binary
            p = set(bin1)
            s = {'0', '1'}
            # IN CASE OF : valid binary input
            if s == p or p == {'0'} or p == {'1'}:
                # Convert input to decimal for limit validation
                x = binary_to_decimal(bin1)
                # IN CASE OF :value out of limit
                if (x > 255 or x < 0):
                    # Out of limit error message
                    print("  x----------------------------------------------------x ")
                    print(" |               __Limit Error__                        |")
                    print(" |  You entered value out of range                      |")
                    print(" |  Please enter a value in range (00000000,11111111)   |")
                    print("  x____________________________________________________x")
                elif(x < 256 or x > 0):
                    # Loop stops when valid binary is given
                    loop2 = True
                else:
                    # error message for invalid input
                    print("--*-- Please give a valid input --*--")
                    # Loop continues
            else:
                # error message for invalid type data input
                print(" ______________________________________________________ ")
                print("|                    _VALUE_ERROR_                     |")
                print("|  Sorry, You did not enter the valid binary digits    |")
                print("|  REMINDER:   Binary digits only contain 0s or 1s     |")
                print("|______________________________________________________|\n")
                # Loop continues
        else:
            # error message for empty input
            print(" ________________________________________________________")
            print("|                 _EMPTY_INPUT_ERROR_                    |")
            print("|           Sorry, You did not enter any digits          |")
            print("|     REMINDER: Binary digits only contain 0s and 1s     |")
            print("|________________________________________________________|\n")
            # Loop continues

    loop3 = False
    # starting a loop for second binary number validation
    # Loop is stopped only when the input is valid
    # loop3 is set true when INPUT is valid
    # loop3 runs until it is false
    while(not loop3):
        # take input as string
        bin2 = str(input("Enter another binary number: ").strip())
        # check empty inputs
        if bin2 != '':
            # Converting input to a set for  checking binary
            p = set(bin2)
            s = {'0', '1'}
            # IN CASE OF : valid binary input
            if s == p or p == {'0'} or p == {'1'}:
                # Convert input to decimal for limit validation
                y = binary_to_decimal(bin2)
                # IN CASE OF :value out of limit
                if (y > 256 or y < 0):
                    # Out of limit error message
                    print("  x----------------------------------------------------x ")
                    print(" |               __Limit Error__                        |")
                    print(" |  You entered value out of range                      |")
                    print(" |  Please enter a value in range (00000000,11111111)   |")
                    print("  x____________________________________________________x")
                elif ((x+y) > 255):
                    # Confirming for the 8-bit adder's sum limit
                    # # Error message for sum out of limit
                    print("  x--------------------------------------------------x ")
                    print(" |                  __Limit Reached__                 |")
                    print(" |      You have already reached the 8-Bit limit      |")
                    print("  x__________________________________________________x")
                    print()
                    print(" PLEASE DON'T MIND THE HASSLE. ENTER THE VALUES AGAIN. \n ")
                    # Calling input methods again
                    return binVal()

                elif(y < 256 or y > 0):
                    # Loop stops when valid binary is given
                    loop3 = True
                else:
                    # error message for invalid input
                    print("--*-- Please give a valid input --*--")
                    # Loop continues
            else:
                # error message for invalid type data input
                print(" ______________________________________________________ ")
                print("|                    _VALUE_ERROR_                     |")
                print("|  Sorry, You did not enter the valid binary digits    |")
                print("|  REMINDER:   Binary digits only contain 0s or 1s     |")
                print("|______________________________________________________|\n")
        else:
            # error message for empty input
            print(" ________________________________________________________")
            print("|                 _EMPTY_INPUT_ERROR_                    |")
            print("|           Sorry, You did not enter any digits          |")
            print("|     REMINDER: Binary digits only contain 0s and 1s     |")
            print("|________________________________________________________|\n")
    print("\nVALUE INPUT SUCCESSFUL\n")
    # TODO - Return the valid binary inputs as decimal digits
    return[x, y]
