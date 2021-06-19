
import secrets
import string
import numpy as np

#Ask user length of password.
n = int(input("Input password length.\n"))
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
#for loop using secrets.choice()
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


#print(pw_initial) #Pool of characters.

#Permute the pool of characters.
pw_final = ''.join(np.random.permutation(pw_initial))

print(f"Your password of length {m} is: \n{pw_final}")

#Check the password. Make sure all characters in the pw_initial pool are included in the final password.

#for i in pw_initial:
#    if i not in pw_final:
#        print("Uh oh")
#else:
#    print("All good!")

#Check pool length and final password length.
#initial_length = len(pw_initial)
#print(initial_length)

#final_length = len(pw_final)
#print(final_length)
