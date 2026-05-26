
def rem(l, word):
    n = []
    for item in l:
        if item in l:
            if not(item == word):
                n.append(item.strip(word))
    return n


n = ["Ansh","Rohan ","Ansh","Rohan","Atul"]

print(rem(n, "Ansh"))

