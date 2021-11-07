import secrets
import string
import numpy as np
import os
import check_input as ci

#Ask user for length of password.
n = input("Please input password length.\n")
n = ci.check_int(n) #Check for non-integer input. Once user inputs an integer, it is converted to type int.
#Password must have at least 8 characters.
while n < 8:
    n = input("Password must have at least eight characters. ")
    n = ci.check_int(n)

m = n #Store the maximum length of the password.

#Create a dictionary for the number of characters to be used in lowercase, uppercase, digits, and special characters.
required_characters = {'lowercase': 'num_lower', 'uppercase': 'num_upper',
 'digits': 'num_digits', 'special_chars': 'num_special'}

#Get category values. ie how many lowercase, uppercase, digits, and special characters.
req_char_values = ci.get_categories(n)
# Set any empty values to zero.
#Avoids IndexError: list index out of range.
if len(req_char_values) < 4: #All 4 categories need values to avoid IndexError.
    for r in range(len(req_char_values), 4):
        req_char_values.append(0) 

index = 0
#Update the required_characters dictionary with the category values.
for key in required_characters.keys():
    required_characters[key] = req_char_values[index]
    index += 1

#Tell the user how password will consist.
print(f"\nYour password of length {m} will consist of the following characters:")
for k, v in required_characters.items():    
    print(f"{k}: {v}")

#Generate the password.
pw_initial = []
print("\n")
for low in range(required_characters['lowercase']):
    low = secrets.choice(string.ascii_lowercase)
    pw_initial.append(low)

for up in range(required_characters['uppercase']):
    up = secrets.choice(string.ascii_uppercase)
    pw_initial.append(up)

for d in range(required_characters['digits']):
    d = secrets.choice(string.digits)
    pw_initial.append(d)

for s in range(required_characters['special_chars']):
    s = secrets.choice(string.punctuation)
    pw_initial.append(s)

print(pw_initial) #Pool of characters.

pw_final = ''.join(np.random.permutation(pw_initial))

print(f"Your password of length {m} is: \n{pw_final}")

#Give the user option to save to a text file, and the option to open that text file.
create_text_file = input("\nWould you like to print this password to a .txt file? ")
while not (create_text_file.lower() == "yes" or create_text_file.lower() == "no"): #Check for nonsense input.
    create_text_file = input("\nWould you like to print this password to a .txt file? Enter yes or no. ")
if create_text_file.lower() == "yes":
    with open('blank_text_file.txt', 'w') as file_object: #blank_text_file.txt is saved in Python file directory.
        file_object.write(pw_final)
        print("Password successfully written to 'blank_text_file.txt'.")        
else:
    quit("Password not saved to .txt file.")

message_open_warning = "\nWould you like to open the text file now? \n\tWARNING: Ensure your screen is not visable to others."
message_open_warning += "\n\tType 'yes' to view the password text file now, or type 'no' to view later. "
view_pw_file = input(message_open_warning)
while not (view_pw_file.lower() == "yes" or view_pw_file.lower() == "no"): #Check for nonsense input.
    view_pw_file = input(message_open_warning)

if view_pw_file.lower() == "yes":
    os.startfile('blank_text_file.txt')
else:
    quit("Password saved in .txt file.")