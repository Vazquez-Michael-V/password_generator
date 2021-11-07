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

def check_remaining_chars(remaining_chars, s):
    """Takes two integers and compares them, remaining_chars < s.
    Will ask user for integer s until remaining_chars < s is satisfied."""      
    while (remaining_chars < s) or (s < 0):         
        s = input(f"Enter a positive integer less than or equal to {remaining_chars}. ")
        s = check_int(s)    
    return s

def get_categories(max_char):
    """Gets number of lowercase letters, number of uppercase letters,
    number of digits, and number of special characters."""
    categories = ['Enter number of lowercase letters. ', 'Enter number of uppercase letters. ', 'Enter number of digits. ', 'Enter number special characters. ']
    remaining_chars = max_char
    while remaining_chars != 0:
        arr = []
        for c in categories:
            c = input(f"{c}")
            c = check_int(c)
            # Check if there are enough characters remaining.
            c = check_remaining_chars(remaining_chars, c)
            remaining_chars -= c        
            #print(max_char)
            #print(remaining_chars)
            arr.append(c)
            print(f"\tYou have {remaining_chars} remaining.")
            if remaining_chars == 0:
                print(f"All {max_char} characters have been used.")                  
                break
        #If password does not meet the required length entered by the user,
        # re-start the process and ask the user to re-enter their specifications.     
        if remaining_chars != 0:    
            print(f"The sum of your entries is less than {max_char}.")
            print("Please re-enter your password specifications.")
            remaining_chars = max_char #Reset the character count.
            continue
        #print(arr)
    return arr
    
#get_categories(10)

