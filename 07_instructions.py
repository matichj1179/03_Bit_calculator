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


# displays instructions / information
def instructions():

    statement_generator("instructions / information", "=")
    print()
    print("please choose a data type (image / text / integer)")
    print()
    print("this program assumes that images are being represented in 24 bit colour (ie: 24 bits per pixel). For text we assmue that ascii encoding is being used (8 bits per character).")
    print()
    print("complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to quit.")
    print()
    return ""

# Main routine
instructions()