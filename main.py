import os
import string

clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

def checkPassword():
    password = input("Enter your password: ")
    validPassword = validatePassword(password)
    if not validPassword:
        return

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
    pass

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
