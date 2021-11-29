Statement = input("Enter your statment: ")


vowels = 0
consonants = 0


VowelsUppercase = ("A", "E", "I", "O", "U")
VowelsLowercase = ("a", "e", "i", "o", "u")


for elements in Statement:
    if elements in VowelsUppercase:
        vowels = vowels + 1 
    elif elements in VowelsLowercase:
        vowels = vowels + 1 
    else:
        consonants = consonants + 1


split_Statement = Statement.split()
IlangSalita = len(split_Statement)



print(("The statement contain:{}".format (IlangSalita) + " words"))
print (f"{vowels}" + " vowels")
print (f"{consonants}" + " consonants")