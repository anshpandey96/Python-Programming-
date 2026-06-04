# Store the multiplication table generated in problem 3 in a file named Table .txt 

n = int(input("Enter a number : "))

table  = [n*i for i in range (1,11)]
with open("table.txt", "a" ) as f:
    f.write(f"Table of {n}: {str(table)} \n")