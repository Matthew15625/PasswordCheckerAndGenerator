def checkPassword():
    pass

def validatePassword(password):
    pass

def calculateScore(password):
    pass

def generatePassword():
    pass

print("Welcome to the password checker and generator. Choose an option from the menu below")
print("1. Check password")
print("2. Generate password")
print("3. Quit")
    
choice = 0
while True:
    choice = input("Pick an option (1/2): ")
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
