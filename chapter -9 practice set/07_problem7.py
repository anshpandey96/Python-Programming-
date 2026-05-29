 
with open("log.txt", "r", encoding="utf-8") as f:

    for lineno, line in enumerate(f, start=1):
        
        if "Python" in line:
            print(f"Yes Python is present. line no: {lineno}")
            break
    else:
        print("No Python is not present")
