import random

reverseDict = {1: "snake", -1: "water", 0: "gun"}
nameToKey = {v: k for k, v in reverseDict.items()}

# get user choice
raw = input(f"Choose one ({', '.join(nameToKey.keys())}): ").strip().lower()
if raw not in nameToKey:
    print("Invalid choice")
    raise SystemExit(1)
you = nameToKey[raw]

# computer choice
computer = random.choice(list(reverseDict.keys()))

print(f"You chose {reverseDict[you]} and Computer chose {reverseDict[computer]}")

if computer == you:
    print("It's a tie!")

elif ((you == -1 and computer == 1) or
      (you == 0  and computer == -1) or
      (you == 1  and computer == 0)):
    print("You win! ")

else:
    print("You lose!")

