import string

AskingForStatement = input("Enter your statement: ")
print (AskingForStatement)

words = 0
vowels = 0
consonants = 0
split_AskingForStatement = AskingForStatement.split()

IlangSalita = len(split_AskingForStatement)

print("The statement contain:{}".format (IlangSalita) + " words")


for statement in AskingForStatement:
    if statement == 'a' or statement == 'e' or statement == 'i' or statement == 'o' or statement == 'u':
        vowels = vowels + 1
    elif statement == 'A' or statement == 'B' or statement == 'I' or statement == 'O' or statement == 'U':
        vowels = vowels + 1
    else:
        consonants = consonants + 1        

print (f"The words inside the statement contain: {vowels} vowels") 
print (f"The words inside the statement also contain these many: {consonants} consonants")
