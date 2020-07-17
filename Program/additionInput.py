from binAdder import *
def addition(x,y):
    # convert the numbers to be added to binary
    m = dec_bin(x)
    n = dec_bin(y)
    # calling the method that adds the binary input 
    # the method also returns the sum as string
    binsum = binAdd(m,n)
    sum = x+y
    if sum<256:
        # in case of the valid sum, the results are appropriately visualised
        print()
        print("x----------x----------x----------x----------x")
        print("   Byte addition process visualised:\n".upper())
        print("    **"+"Decimal"+"**    **"+" Binary**")
        print()
        print("        "+"{:0>3d}".format(x)+"          "+m.zfill(8) )
        print("      + "+"{:0>3d}".format(y)+"        + "+n.zfill(8) )
        print("       "+"-----"+"        "+"----------")
        print("        "+"{:0>3d}".format(sum)+"          "+str(binsum))
        print()
        print("x----------x----------x----------x----------x")
    # else:
    #     print("  x----------------------------------------------------x ")
    #     print(" |               __Limit Error__                        |")
    #     print(" |  Sum cannnot be more than 255 i.e bin(11111111)      |")
    #     print(" |  Please use the byte adder accordingly.              |")
    #     print("  x____________________________________________________x")
