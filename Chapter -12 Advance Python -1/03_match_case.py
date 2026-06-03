def check_number(x):
    match x:
        case 10:
            print("It's 10")
        case 20:
            print("It's 20")
        case _:
            print("It's neither 10 nor 20")

check_number(10)   # Output: It's 10
check_number(30)   # Output: It's neither 10 nor 20

