import os
import string

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

def calculateScore(password):
    score = len(password)
    containsAllDifferentTypesOfCharacter = True
    
    # checking for a lowercase
    found = False
    for char in password:
        if char in string.ascii_lowercase:
            score += 5
            found = True
            break
    containsAllDifferentTypesOfCharacter = containsAllDifferentTypesOfCharacter and found
    
    # checking for an uppercase
    found = False
    for char in password:
        if char in string.ascii_uppercase:
            score += 5
            found = True
            break
    containsAllDifferentTypesOfCharacter = containsAllDifferentTypesOfCharacter and found

    # checking for a digit
    found = False
    for char in password:
        if char in string.digits:
            score += 5
            found = True
            break
    containsAllDifferentTypesOfCharacter = containsAllDifferentTypesOfCharacter and found

    # checking for a symbol
    found = False
    for char in password:
        if char in "!$%^&*()-_=+":
            score += 5
            found = True
            break
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
            onlyLetters = False
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
    for i in range(len(password - 2)):
        for row in qwerty:
            if password[i:i+3] in row:
                score -= 5
    
    return score

def generatePassword():
    pass

def displayMenu():
    clear()
    print("Welcome to the password checker and generator. Choose an option from the menu below")
    print("1. Check password")
    print("2. Generate password")
    print("3. Quit")

    choice = 0
    while True:
        choice = input("Pick an option (1/2/3): ")
        try:
            choice = int(choice)
            if choice in [1, 2, 3]:
                break
        except:
            pass

        print("Please enter a 1, 2 or 3.")
        
    if choice == 1:
        print("checking password")
        checkPassword()
    elif choice == 2:
        print("generating password")
        generatePassword()
    else:
        exit()
    input("Press enter to return to the menu")
    displayMenu()

displayMenu()
