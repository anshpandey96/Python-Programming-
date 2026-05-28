f = open("file.txt")

print(f.read())
f.close()


#the same can be done using with statement like

with open("file.txt") as f:
    print(f.read())

# you dont have to explicitly close the file when you use with statement, it will automatically close the file after the block of code is executed. 
