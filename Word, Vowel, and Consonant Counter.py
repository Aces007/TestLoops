# This will prompt you "the user" for the statement you want to analyze for words, vowels, and consonants.
Statement = input("Please enter your statement: ")

# Now these two variables record the number of the vowels and consonants that is presented by the print functions below.  
vowels = 0
consonants = 0

# These variables now are responsible for defining the vowels below and what they contain.   
VowelsUppercase = ("A", "E", "I", "O", "U")
VowelsLowercase = ("a", "e", "i", "o", "u")

# Now this for loop is responsbile for initializing the count for the vowels and consonants.
for elements in Statement:
    if elements in VowelsUppercase:
        vowels = vowels + 1 
    elif elements in VowelsLowercase:
        vowels = vowels + 1 
    else:
        consonants = consonants + 1

# Independently, these two lines count the words found on the sentences stated above. They are presented by the print function below.
split_Statement = Statement.split()
IlangSalita = len(split_Statement)

# Lastly, these print funtions are responsible for presenting you the number of the words including the vowels and consonants each words contain.
print(("The statement contain:{}".format (IlangSalita) + " words"))
print (f"{vowels}" + " vowels")
print (f"{consonants}" + " consonants")