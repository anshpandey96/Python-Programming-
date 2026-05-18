a = " Ansh is a good boy\nbut not a bad 'boy'"

print(a)


# \n — Newline
print("Hello\nWorld")
# Hello
# World

# \t — Tab
print("Name:\tAlice")
# Name:    Alice

# \\ — Literal backslash
print("C:\\Users\\Alice")
# C:\Users\Alice

# \' and \" — Quotes inside strings
print('It\'s a sunny day')
print("She said \"Hello\"")

# \b — Backspace
print("Hello\bWorld")   # HelloWorld (erases 'o')

# \r — Carriage return
print("Hello\rWorld")   # World (overwrites from start)

# Hex and Unicode
print("\x48\x65\x6C\x6C\x6F")  # Hello
print("\u2764")                  # ❤
print("\U0001F600")              # 😀
print("\N{LATIN SMALL LETTER A}")  # a


