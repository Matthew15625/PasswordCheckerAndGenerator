import os
import string
import random

clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

def checkPassword():
    password = input("Enter your password: ")
    validPassword = validatePassword(password)
    if not validPassword:
        return
    score = calculateScore(password)
    strength = ""
    if score <= 0:
        strength = "weak"
    elif score <= 20:
        strength = "medium"
    else:
        strength = "strong"
    
    print("Your password's score is " + str(score) + ", and the strength is " + strength + ".")

def validatePassword(password):
    if len(password) in range(8, 25):
        allowed = string.ascii_letters + string.digits + "!$%^&*()-_=+"
        for char in password:
            if char not in allowed:
                print("Your password must only contain the allowed characters:", allowed)
                return False
    else:
        print("Your password must be between 8 and 24 characters long.")
        return False
    return True

def checkPasswordFor(password, searchString):
    found = False
    for char in password:
        if char in searchString:
            found = True
            break
    return found

def calculateScore(password):
    score = len(password)
    containsAllDifferentTypesOfCharacter = True

    # checking for a lowercase
    found = checkPasswordFor(password, string.ascii_lowercase)
    if found:
        score += 5
    containsAllDifferentTypesOfCharacter = containsAllDifferentTypesOfCharacter and found
    
    # checking for an uppercase
    found = checkPasswordFor(password, string.ascii_uppercase)
    if found:
        score += 5
    containsAllDifferentTypesOfCharacter = containsAllDifferentTypesOfCharacter and found

    # checking for a digit
    found = checkPasswordFor(password, string.digits)
    if found:
        score += 5
    containsAllDifferentTypesOfCharacter = containsAllDifferentTypesOfCharacter and found

    # checking for a symbol
    found = checkPasswordFor(password, "!$%^&*()-_=+")
    if found:
        score += 5
    containsAllDifferentTypesOfCharacter = containsAllDifferentTypesOfCharacter and found

    if containsAllDifferentTypesOfCharacter:
        score += 10

    onlyLetters = True
    for char in password:
        if char not in string.ascii_letters:
            onlyLetters = False
            break
    if onlyLetters:
        score -= 5
    
    onlyDigits = True
    for char in password:
        if char not in string.digits:
            onlyDigits = False
            break
    if onlyDigits:
        score -= 5
    
    onlySymbols = True
    for char in password:
        if char not in string.digits:
            onlySymbols = False
            break
    if onlySymbols:
        score -= 5
    
    qwerty = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    for i in range(len(password) - 2):
        for row in qwerty:
            if password[i:i+3] in row:
                score -= 5
    
    return score

def generatePassword():
    password = ""
    length = random.randint(8, 12)
    score = 0
    while score <= 20:
        password = ""
        for i in range(length):
           password += random.choice(list(string.ascii_letters + string.digits + "!$%^&*()-_=+"))
        score = calculateScore(password)
    print("Your password is " + password + ", and its score is " + str(score) + ".")

def displayMenu():
    clear()
    print("Welcome to the password checker and generator. Choose an option from the menu below")
    print("1. Check password")
    print("2. Generate password")
    print("3. Quit")

    while True:
        choice = input("Pick an option (1/2/3): ")
        if choice in ["1", "2", "3"]:
            break

        print("Please enter a 1, 2 or 3.")
        
    if choice == 1:
        checkPassword()
    elif choice == 2:
        generatePassword()
    else:
        exit()
    input("Press enter to return to the menu...")
    displayMenu()

displayMenu()
