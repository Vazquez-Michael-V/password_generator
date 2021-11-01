def check_int(input_int):
    """Checks if user input is an integer.
    Loop runs until the user inputs an integer.
    User input is then converted to type int."""
    while True:
        try:
            input_int = int(input_int)
        except ValueError:
            print("Input must enter an integer.")
            input_int = input("\tPlease enter an integer. ")
        else:
            input_int = int(input_int)
            return input_int
         
            

