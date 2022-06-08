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


