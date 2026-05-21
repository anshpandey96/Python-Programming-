p1 = "Make a lot of maney"
p2 = "subacribe this"
p3 = "buy now"
p4 = "click this"

message = input("Enter your commnet: ")

if((p1 in message) or (p2 in message ) or (p3 in message ) or (p4 in message)):
    print("This comment is a spam")

else:
    print("This comment is not a spam")    

