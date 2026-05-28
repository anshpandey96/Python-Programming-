# f = open("file.txt")

# # Method 1: readlines() - saari lines ek saath list mein
# lines = f.readlines()
# for line in lines:
#     print(line, end="")

# f.close()

# lines = f.readlines()
# print(lines, type(lines))

# line1 = f.readline()
# print(line1, type(line1))
# line2 = f.readline()
# print(line2, type(line2))
# line3 = f.readline()
# print(line3, type(line3))
# linen = f.readline()
    
# print(line5 == "")
# lines = f.readlines()
# while(lines != ""):
#     print(lines)

# lines = f.readline()
# f.close()

# f = open("file.txt")

# Method 1: readlines()
f = open("file.txt")
lines = f.readlines()
for line in lines:
    print(line, end="")
f.close()

print("---")  # separator

# Method 2: readline() with while loop
f = open("file.txt")
line = f.readline()
while line != "":
    print(line, end="")
    line = f.readline()
f.close()