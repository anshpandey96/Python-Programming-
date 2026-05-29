with open("log.txt") as f:
    contents = f.read()

    if("Python" in contents):
        print("Yes Python is present")

    else:
        print("This is not present>>")
