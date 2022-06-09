def num_check(question, low):

    valid = False
    while not valid:

        error = "please enter a interger that is more than (or eqaul to) {}".format(low)

        try:
            response = int(input(question))

            if response >= low:
                return response

            else:
                print(error)
                print()

        except ValueError:
            print(error)


# converts decimal to binary and states how
# many bits are needed to represent the original interger
def int_bits():

    # get integer (must be >= 0)
    var_integer = num_check("please enter an integer: ", 0)

    # source code below is
    # https://stackoverflow.com/questions/699866/python-int-to-binary-string

    var_binary = "{0:b}".format(var_integer)

    # calculate # of bits (length of string above)
    num_bits = len(var_binary)

     # output answer with working
    print()
    print("{} in binary is {}".format(var_integer, var_binary))
    print("# of bits is {".format(num_bits))
    print()

    return ""
    
#main routine
int_bits()

 