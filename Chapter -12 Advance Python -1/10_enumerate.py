l = [3,532,62,71]


# index = 0
# for item in l:
#     index += 1
#     print(f"The item number{index} is {item}")
#     index += 1      

# This can be simplified using enumerate Function


for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")