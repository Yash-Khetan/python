# roll a dice ?
# if yes generate two random numbers 
# if no print thanks for playing 
# else continue the question of rolling a dice ?

import random
import math
play = True
while play is True:
    a = raw_input("Roll a dice ?(y/n)").lower()
    if a == "y":
        print(random.randint(1,6),random.randint(1,6))
    elif a == "n":
        print("Thanks for playing!")
        play = False
        break
    else:
        print("Invalid choice")

    
