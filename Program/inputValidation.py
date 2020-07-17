# TODO - Import necessary modules required
import validBinary,validDecimal

# TODO - Make a method that asks for the decision between binary or decimal input
def inputValidation1():
    loop = False
        #Initially loop is set as false
        # The loop runs until it is set as true 
    while(not loop):
        # ASK FOR: decision between binary or decimal addition
        BorD = input("\nEnter binary or decimal (B/D) or (b/d):")
        # IN CASE OF : Binary
        if str(BorD).upper().strip()=='B':
            print("\nYou entered binary\n".upper())
            print("Now, please enter the binary values below.")
            # method to validate binary input is called
            return(validBinary.binVal())
            break 
        # IN CASE OF : Decimal               
        elif str(BorD).upper().strip()=='D':         
            print("\nYou decided decimal.\n".upper())
            print("Now, Please enter the decimal values below.")
            # method to validate decimal input is called
            return(validDecimal.decVal())
            break 
        # IN CASE OF : Empty input 
        elif str(BorD).upper().strip()=="":
            # Error message is given with proper instructions
            print("x--------------------------------------x")
            print("|          EMPTY INPUT                 |")
            print("| You did not enter any characters     |")
            print("| YOU CAN ONLY ENTER EITHER B,b OR D,d |")
            print("x--------------------------------------x\n")
            print("Please provide your decision again.")
        else:
            # Error message is given with proper instructions
            print("x-------------------------------------------x")
            print("|      INVALID CHARACTER ERROR              |")
            print("|  YOU CAN ONLY ENTER EITHER B,b OR D,d     |")
            print("x-------------------------------------------x")            
            print(str(BorD) + " is an invalid input.\n")
            print("Please provide your decision again.")
  
