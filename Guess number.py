# Guess Random Number

import random

random_number = random.randint(0, 5)
user_number = input("Guess the number from 0 to 5: ")

if user_number == random_number:
    print("You are right!")
else:
    print("You can't guess this number!")
    
print(f"Guess number is:  {random_number}")
