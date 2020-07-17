# declaring decimal validation method
def decVal():
    # TODO - Print Instructions on decimal addition process
    print("NOTE: The decimal value must lie in between 1 and 256(exclusively).\n")
    loop2 = False
    # starting a loop for first decimal number validation
    # Loop is stopped only when the input is valid
    # loop2 is set true when INPUT is valid
    # loop2 runs until it is false
    while(not loop2):
        # Initiate a try-catch block for exception handling
        try:
            # take input as string
            dec1 = input("Enter a decimal number: ").strip()
            # check empty inputs
            if dec1.strip() != '':
                # Converting input to a int for checking decimal
                decimal1 = int(dec1)
                # IN CASE OF :value out of limit
                if (decimal1 > 255 or decimal1 < 0):
                    # Out of limit error message
                    print("  x----------------------------------------------------x ")
                    print(" |               __Limit Error__                        |")
                    print(" |  You entered value out of range                      |")
                    print(" |  Please enter a value in range (1,256) exclusively   |")
                    print("  x____________________________________________________x\n")
                elif(decimal1 < 256 or decimal1 > 0):
                    # Loop stops when valid decimal is given
                    loop2 = True
                else:
                    # error message for invalid input
                    print("--*-- Please give a valid input --*--")
            else:
                # error message for empty input
                print(" ________________________________________________________")
                print("|                 _EMPTY_INPUT_ERROR_                    |")
                print("|           Sorry, You did not enter any digits          |")
                print("|              Do enter a valid decimal digit            |")
                print("|________________________________________________________|\n")

        except ValueError:
            # error message for invalid data type input
            print(" ______________________________________________________ ")
            print("|                     _VALUE_ERROR_                    |")
            print("|  Sorry, You did not enter the valid decimal digits.  |")
            print("|                     Do try again                     |")
            print("|______________________________________________________|\n")
    loop3 = False
    # starting a loop for second decimal number validation
    # Loop is stopped only when the input is valid
    # loop3 is set true when INPUT is valid
    # loop3 runs until it is false
    while(not loop3):
        # Initiate a try-catch block for exception handling
        try:
            # take input as string
            dec2 = input("Enter another decimal number: ").strip()
            # check empty inputs
            if dec2.strip() != '':
                # Converting input to a int for checking decimal
                decimal2 = int(dec2)
                # IN CASE OF :value out of limit
                if (decimal2 > 256 or decimal2 < 0):
                    print("  x----------------------------------------------------x ")
                    print(" |               __Limit Error__                        |")
                    print(" |  You entered value out of range                      |")
                    print(" |  Please enter a value in range (1,256) exclusively   |")
                    print("  x____________________________________________________x\n")
                elif ((decimal1+decimal2) > 255):
                    # Confirming for the 8-bit adder's sum limit
                    # # Error message for sum out of limit
                    print("  x--------------------------------------------------x ")
                    print(" |                  __Limit Reached__                 |")
                    print(" |      You have already reached the 8-Bit limit      |")
                    print("  x__________________________________________________x")
                    print()
                    print("    PLEASE DON'T MIND THE HASSLE. ENTER THE VALUES AGAIN\n ")
                    return decVal()

                elif(decimal2 < 256 or decimal2 > 0):
                    # Loop stops when valid binary is given
                    loop3 = True
                else:
                    # error message for invalid input
                    print("--*-- Please give a valid input --*--")
                    # Loop continues
            else:
                # error message for empty input
                print(" ________________________________________________________")
                print("|                 _EMPTY_INPUT_ERROR_                    |")
                print("|           Sorry, You did not enter any digits          |")
                print("|              Do enter a valid decimal digit            |")
                print("|________________________________________________________|\n")

        except ValueError:
            # error message for invalid data type input
            print(" ______________________________________________________ ")
            print("|                     _VALUE_ERROR_                    |")
            print("|  Sorry, You did not enter the valid decimal digits.  |")
            print("|                     Do try again                     |")
            print("|______________________________________________________|\n")
        except:
            # raise the exception
            raise
    print("\nVALUE INPUT SUCCESSFUL")
    # TODO - Return the valid decimal digits
    return[decimal1, decimal2]
