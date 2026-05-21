marks1 = int(input("Enter  the marks subject 1:"))
marks2 = int(input("Enter  the marks subject 2:"))
marks3 = int(input("Enter  the marks subject 3:"))

total_percentage =  (100*(marks1+marks2+marks3))/300

if(total_percentage>= 40 and marks3>33 and marks2>33):
    print("You are pass ",total_percentage)

else:
    print("You failed, try again next year!",total_percentage)
