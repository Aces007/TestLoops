# The importing of this regular expression specifies a certain expression that matches with the given conditions in your program.
import re

# To begin with, this first line will ask you for a new password, it will have its criteria prepared on the event you are typing your combinations.
CreateNewPassword = input("Enter a new password: ")
# This line record the chances you have for verifying your entered password. 
Chances = 8
# Now these 4 lines here records the characters your password contain including the capital letters, numbers, and sepcial characters.  
CharactersPo = (len(CreateNewPassword))
CapitalLettersNaman = len(re.findall (r'[A-Z]', CreateNewPassword))
NumbersAsWell = sum(characters.isdigit() for characters in CreateNewPassword)
LastlySpecialCharacters = len(CreateNewPassword) - len(re.findall ('[\w]', CreateNewPassword))

# Then these print functions presents the quantity for each variable.
print (CharactersPo)
print (CapitalLettersNaman)
print(NumbersAsWell)
print (LastlySpecialCharacters)

# Now these 4 functions are responsible for checking your passwords validity and if you have matched with the criteria on the algorithm.
def Characters():
    if CharactersPo >= 15:
        print ("Now let's check the numbers, special characters and letters incorporated in your combination")
    else: 
        print ("The minimum characters count required is 15, add more characters if you may")
        EnterAnotherOne  = input("Enter a new password: ")
        return EnterAnotherOne

# This is for evaluating your passwords content for letters specifically Uppercase ones.
def CapitalLetters():
    if CapitalLettersNaman >= 1:
        print ("Okay, now for the Numbers")
    else:
        print ("To create a stronger password, incorporate Capital Letters, Numbers and Special Characters")
        EnterOneAgain = input("Enter a new password: ")
        return EnterOneAgain

# Then, this is for checking if the password has numbers. 
def Numbers():
    if NumbersAsWell >= 1:
        print ("Okay, lastly the Special Characters")
    else:
        print ("To create a stronger password, incorporate Capital Letters, Numbers and Special Characters")
        EnterItAgainPlease = input("Enter a new password: ")
        return EnterItAgainPlease

# Lastly, this is for checking if you have special characters included to make your password stronger, if not met the program will tell you 
# that you have not satisifed the conditions and will prompt you to enter a much stronger password.
def SpecialCharacters():
    if LastlySpecialCharacters >= 1:
        print ("You have met all the criteria")
    else: 
        print ("You have not met the criteria") 
        print ("Create a stronger combination")
        EnterAStrongerPassword = input("Enter a new password: ")
        return EnterAStrongerPassword

# These lines will call the functions. 
EnterAnotherOne = Characters()
EnterOneAgain = CapitalLetters()
EnterItAgainPlease = Numbers()
EnterAStrongerPassword = SpecialCharacters()

# Then this will initialize if the requirements are met. This will now evaluate your password if they are the same and valid. 
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
# If not you will be deducted attempts for evaluating your password until you have ran out and you are locked out of your account.
# But if you have evaluated your password successfully, you are granted access to your account and will be presented with the chances you have 
# left for typing your passwords multiple times.
if statement == 1:
    print ("Your account is locked temporarily")
else:
    print ("Access Granted")    
print ("Attempts: {}".format (Chances) + " chances left")