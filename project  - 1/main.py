'''
1  = snake 
-1 = water 
0  = gun 
'''

import random

# Computer random choice karega
computer = random.choice([1, -1, 0])

you = input("Enter your choice (snake / water / gun): ")

youDict = {"snake": 1, "water": -1, "gun": 0}
you = youDict[you]

# Result
if computer == you:
    print("It's a tie! ")

elif (you == 1  and computer == -1) or \
     (you == 0  and computer == 1)  or \
     (you == -1 and computer == 0):
    print("You win! 🎉")

else:
    print("You lose! ")

