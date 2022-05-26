def num_check(question, low):

    valid = False
    while not valid:

        error = "please enter a interger that is more than "
        "(or eqaul to) {}".format(low)

        try:
            response = int(input(question))

            if response >= low:
                return response

            else:
                print(error)
                print()

        except ValueError:
            print(error)





# Main Routine goes here

keep_going = ""
while keep_going == "":
    print()
    #ask the user for an interger (must be more than / eqaul to 0)
    var_inter = num_check("enter a integer:  ", 0)
    print()

    # ask for the width & height of an image
    # (must be more tha / eqaul to 1)
    image_width = num_check("image width? ", 1)
    print() 
    image_height = num_check("image height?", 1)