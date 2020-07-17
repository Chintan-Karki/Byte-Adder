# TODO - Import necessary modules required
import inputValidation
import additionInput

# Declaring a method to initialize the program


def mainfunction():
    """ All the welcome texts 
        during the execution of the program"""

    print("  _____       _   _                   ____        _                     _     _           ")
    print(" |  __ \     | | | |                 |  _ \      | |           /\      | |   | |          ")
    print(" | |__) |   _| |_| |__   ___ __ __   | |_) |_   _| |_ ___     /  \   __| | __| | ___ _ __ ")
    print(" |  ___/ | | | __| '_ \ / _ \| '_ \  |  _ <| | | | __/ _ \   / /\ \ / _` |/ _` |/ _ \ '__|")
    print(" | |   | |_| | |_| | | | (_) | | | | | |_) | |_| | ||  __/  / ____ \ (_| | (_| |  __/ |   ")
    print(" |_|    \__, |\__|_| |_|\___/|_| |_| |____/ \__, |\__\___| /_/    \_\__,_|\__,_|\___|_|   ")
    print("         __/ |                               __/ |                                        ")
    print("        |___/                               |___/                                         ")
    print("ⓒ ⓗ ⓘ ⓝ ⓣ ⓐ ⓝ   ⓚ ⓐ ⓡ ⓚ ⓘ")
    print("ⓘ ⓘ ⓒ\n\n")
    print("x----------x-----Welcome to the byte adder program-----x----------x\n")
    #  Instructions to follow during the execution of program
    print(" _____________________________________________________________ ")
    print("|                  _THINGS TO CONSIDER_                       |")
    print("|                                                             |")
    print("| 1. You can use this adder program to add                    |")
    print("|    either binary or decimal up-to 8bits(1byte).             |")
    print("| 2. You can perform addition upto of 255(d) or 11111111(b)   |")
    print("| 3. Enter your choice : binary or decimal below              |")
    print("|_____________________________________________________________|\n")

    # TODO : Call the input method and validate the input
    arr = inputValidation.inputValidation1()
    # After input validation addition of inputs is done through the 'additionInput' method
    # The addition is done only :
    # after the validated values are passed as array to the 'additionInput' method
    additionInput.addition(arr[0], arr[1])
    # Loop started for next round of addition
    mainloop = False
    # Loop runs only if boolean value of 'mainloop' is false
    while(not mainloop):
        # TODO - Ask for decision from the user for running the program again
        YorN = str(input(
            "\nDo you want to run the byte adder again?\n\nEnter your decision (Y/N) or (y/n): "))
        if YorN.upper().strip() == 'Y':
            # TODO - Remind the user about byte adder, and all of its rule
            # Its important to remind them of 8-bit adders
            print(" _____________________________________________________________ ")
            print("|                    _GENTLE REMINDERS_                       |")
            print("| 1. You can use this adder program to add                    |")
            print("|    either binary or decimal up-to 8bits(1byte).             |")
            print("| 2. You can perform addition upto of 255(d) or 11111111(b)   |")
            print("| 3. Enter your choice : binary or decimal below              |")
            print("|_____________________________________________________________|\n")

            # TODO : Call the input method and validate the input
            arr = inputValidation.inputValidation1()
            # After input validation addition of inputs is done through the 'additionInput' method
            # The addition is done only :
            # after the validated values are passed as array to the 'additionInput' method
            additionInput.addition(arr[0], arr[1])
        elif YorN.upper().strip() == '':
            # IN CASE OF :empty inputs
            # TODO - Ask users again for valid input
            print(" ___________________________________________________ ")
            print("|               _EMPTY INPUT ERROR_                 |")
            print("|        You did not enter any character.           |")
            print("|         Please enter Y/y or N/n only.             |")
            print("|___________________________________________________|\n")
            # Loop continues
        elif YorN.upper().strip() == 'N':
            # IN CASE OF :ending decision
            # TODO - Ending message and closing the program
            print(" _____________________________________________________________ ")
            print("|       _THANK YOU FOR USING THE BYTE ADDER PROGRAM_          |")
            print("|                                                             |")
            print("|                    Have a good day!!                        |")
            print("|_____________________________________________________________|\n")
            # Loop to be closed
            mainloop = True
        else:
            # IN CASE OF special characters,
            # program asks for the valid inputs through message
            print(" \n___________________________________________________ ")
            print("|            _INVALID INPUT ERROR_                  |")
            print("|    You did not enter a valid input character.     |")
            print("|        Please enter Y/y or N/n only.              |")
            print("|___________________________________________________|\n")

            # Loop continues
# Running the program by calling main method
mainfunction()
