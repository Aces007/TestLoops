import re

CreateNewPassword = input("Enter a new password: ")
Chances = 8
CharactersPo = (len(CreateNewPassword))
CapitalLettersNaman = len(re.findall (r'[A-Z]', CreateNewPassword))
NumbersAsWell = sum(characters.isdigit() for characters in CreateNewPassword)
LastlySpecialCharacters = len(CreateNewPassword) - len(re.findall ('[\w]', CreateNewPassword))

print (CharactersPo)
print (CapitalLettersNaman)
print(NumbersAsWell)
print (LastlySpecialCharacters)

def Characters():
    if CharactersPo >= 15:
        print ("Now let's check the numbers, special characters and letters incorporated in your combination")
    else: 
        print ("The minimum characters count required is 15, add more characters if you may")
        EnterAnotherOne  = input("Enter a new password: ")
        return EnterAnotherOne

def CapitalLetters():
    if CapitalLettersNaman >= 1:
        print ("Okay, now for the Numbers")
    else:
        print ("To create a stronger password, incorporate Capital Letters, Numbers and Special Characters")
        EnterOneAgain = input("Enter a new password: ")
        return EnterOneAgain

def Numbers():
    if NumbersAsWell >= 1:
        print ("Okay, lastly the Special Characters")
    else:
        print ("To create a stronger password, incorporate Capital Letters, Numbers and Special Characters")
        EnterItAgainPlease = input("Enter a new password: ")
        return EnterItAgainPlease

def SpecialCharacters():
    if LastlySpecialCharacters >= 1:
        print ("You have met all the criteria")
    else: 
        print ("You have not met the criteria") 
        print ("Create a stronger combination")
        EnterAStrongerPassword = input("Enter a new password: ")
        return EnterAStrongerPassword

EnterAnotherOne = Characters()
EnterOneAgain = CapitalLetters()
EnterItAgainPlease = Numbers()
EnterAStrongerPassword = SpecialCharacters()


for statement in range(8, 0 , -1):
    MagkaparehasBa = input("Enter Password Again: ")
    if CreateNewPassword == MagkaparehasBa:
        break
    elif EnterAnotherOne == MagkaparehasBa:
        break
    elif EnterOneAgain == MagkaparehasBa:
        break
    elif EnterItAgainPlease == MagkaparehasBa:
        break
    elif EnterAStrongerPassword == MagkaparehasBa:
        break
    else:
        print ("Incorrect password, Try again!")  
        Chances = Chances - 1

if statement == 1:
    print ("Your account is locked temporarily")
else:
    print ("Access Granted")    
print ("Attempts: {}".format (Chances) + " chances left")