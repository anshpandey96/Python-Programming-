# name = (input("Enter your name:"))
# print("Dear<|"+ name + "|>")
# print("Are you selected !")
# print("<|Date|>")


letter = '''Dear <|Name|> , 
You are selected !
<|Date|>'''

print(letter.replace("<|Name|>", "Ansh").replace("<|Date|","24 september 2050"))

