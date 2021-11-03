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
         
def get_categories():
    """Gets number of lowercase letters, number of uppercase letters,
    number of digits, and number of special characters."""
    categories = ['Enter number of lowercase letters. ', 'Enter number of uppercase letters. ', 'Enter number of digits. ', 'Enter number special characters. ']
    arr = []
    for c in categories:
        c = input(f"{c}")
        c = check_int(c)
        while c <0: #Can't have negative number of characters. ie no -5 lowercase letters.
            c = input("Integer must be positive. ")
            c = check_int(c)
        arr.append(c)
    return arr

def check_remaining_chars(remaining_chars, s):
    """Takes two integers and compares them, remaining_chars < s.
    Will ask user for integer s until remaining_chars < s is satisfied."""      
    while (remaining_chars < s) or (s < 0):
        s = input(f"Enter a positive integer less than or equal to {remaining_chars}. ")
        s = check_int(s)