# declaring methods that act as OR, AND and XOR gates
# These methods returnthe same output as real logic gates


def orGate(b1, b2):
    return b1 | b2


def andGate(b1, b2):
    return b1 & b2


def xorGate(b1, b2):
    return b1 ^ b2

# declaring a method that converts decimal integer to binary string


def dec_bin(num):
    # declaring a 8- bit binary arrray of 0
    c = ["0", "0", "0", "0", "0", "0", "0", "0"]
    i = 7
    while (num > 0):
        r = num % 2
        c[i] = str(r)
        i = i-1
        num = int(num/2)
    # return a string as binary
    return "".join(c)

# declaring a method that converts binary integer to decimal integer


def binary_to_decimal(num):

    i, integer = 0, 0
    size = len(num)
    while i < size:
        integer += int(num[size - 1 - i])*pow(2, i)
        i += 1
    # return a integer of decimal
    return integer

# declare a method to add two binary digits


def binAdd(num1, num2):
    # declare a array with empty 8 zero
    # this array is modified with each loop
    # Finally this array morphs to 8 bit sum
    arrSum = ["0", "0", "0", "0", "0", "0", "0", "0"]
    # default carry value is 0
    carry = 0
    i = 7
    # inputs are converted to integers
    x = int(num1)
    y = int(num2)
    # greater input is identified
    maxBin = max(x, y)
    # loop continues until greater input is more than 0
    while(maxBin > 0):
        # Extracting the last bits of binary
        # For example: from 1010, we take last bit i.e. 0
        r1 = x % 10
        r2 = y % 10
        # using logic gates for sum calculation
        # SUM calculation
        xor1 = xorGate(r1, r2)
        sumBin = xorGate(xor1, carry)

        # For Carry
        # Carry for next loop is calculated here
        and1 = andGate(r1, r2)
        and2 = andGate(xor1, carry)
        carry = orGate(and1, and2)

        # The i'th element is modified in arrSum
        # Initially , i is 7 and decreases by 1 with each loop
        arrSum[i] = str(sumBin)
        i = i-1
        # Last digits are thrown out
        maxBin = int(maxBin/10)
        x = int(x/10)
        y = int(y/10)

    if i >= 0:
        arrSum[i] = str(carry)
    # finally a string with valid sum of binary is returned
    return "".join(arrSum)
