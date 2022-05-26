# Functions go here

# Puts series of symbols at the start and end of text (for emphasis)
def statement_generator(text, decoration):

    # Make string with five characters
    ends = decoration * 5

    #  add decoration to start and end of statements
    statement = "{} {} {}".format(ends, text, ends)

    print ()
    print(statement)
    print ()

    return ""

#checks user choice is 'interger', 'text' or 'image'
def user_choice():


    # Lists of valid reponses
    text_ok = ["text", "t", "txt"]
    integer_ok = ["integer", "int", "#", "number"]
    image_ok = ["image", "img", "p", "picture", "pic"]

    valid = False
    while not valid:

        # ask user for choice and change response to lower case

        response = input ("file type (integer / text / image): ").lower()

        #checks for valid response and returns text, integer or image

        if response in text_ok:
            return "text"

        elif response in integer_ok:    
            return "integer"

        elif response in image_ok:
            return "image"

        elif response == "i":
            want_integer = input("press <enter> for an integer or any key for image")
            if want_integer == "":
                return "integer"
            else:
                return "image"

        else:
            # if response is not valid, output and error
            print("please choose a valid file type!")
            print()

# check input is a number more than a given value
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

# Heading
statement_generator("bit calculator for Integers, Text & Images", "-")


# Main routine goes here
print()

keep_going = ""
while keep_going == "":


    data_type = user_choice()
    print("you chose", data_type)
    print()
    
    # for intgers, ask for integer
    if data_type =="integer":
        var_integer = num_check("enter an integer: ", 0)

    # for images, ask for width and height
    # (must be an integer mare than / eqaul to 0)
    elif data_type == "image":
        image_width = num_check("image width? ", 1)
        print() 
        image_height = num_check("image height?", 1)
    
    # for text, ask for a string
    else:
        var_text = input(" enter some text: ")

    keep_going = input("Press <enter> to keep going or any key to quit")

    print()
    print("Thanks for using the bit calculator")
    print()
