import string

AskingForStatement = input("Enter your statement: ")
print (AskingForStatement)


words = 0
vowels = 0
consonants = 0


split_AskingForStatement = AskingForStatement.split()
IlangSalita = len(split_AskingForStatement)
print("The statement contain:{}".format (IlangSalita) + " words")

VowelsCapital = ["A", "E", "I", "O", "U"]
VowelsLowercase = ['a', 'e', 'i', 'o', 'u']


for words in AskingForStatement:
    if words == 'a' or words == 'e' or words == 'i' or words == 'o' or words == 'u':
        vowels = vowels + 1
    elif words == 'A' or words == 'B' or words == 'I' or words == 'O' or words == 'U':
        vowels = vowels + 1
    else:
        consonants = consonants + 1        

print (f"The words inside the statement contain: {vowels} vowels") 
print (f"The words inside the statement also contain these many: {consonants} consonants")
