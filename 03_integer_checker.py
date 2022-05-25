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

