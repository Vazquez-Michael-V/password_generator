
import secrets
import string
import numpy as np
import os

#Ask user length of password.
n = input("Input password length.\n")

#Check for nonsense input and passwords less than eight characters.
while True:
    while n.isnumeric() == False:
        n = input("Password length must be an integer greater than or equal to eight. ")
        continue
    if int(n) < 8:
        n = input("Password must have at least eight characters. ")
    else:
        break
        
n = int(n)        
m = n

#Store these values in a dictionary.
required_characters = {'lowercase': 'num_lower', 'uppercase': 'num_upper',
 'digits': 'num_digits', 'special_chars': 'num_special'}

for k, v in required_characters.items():
    v = input(f"Enter {v}. ")    
    while v.isnumeric() == False:
        v = input(f"\tEnter an integer. ")
    else:
        v = int(v)
        #Check if the sum is equal to n.
        n = n - v 
        #print(n)
        required_characters[k] = v       
        if n > 0:            
            print(f"You have {n} available.")              
    #Unassigned values get set to zero.
        else:
            print(f"\nAll {m} characters have been used.")
            break

#Tell the user how password will consist.
print(f"\nYour password of length {m} will consist of the following characters:")
for k, v in required_characters.items(): 
    if isinstance(v, int) == False: 
        v = 0
        required_characters[k] = v   
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
    create_text_file = input("\nWould you like to print this password to a .txt file? ")
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