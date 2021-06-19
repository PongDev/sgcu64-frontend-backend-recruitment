#! /usr/bin/python3

# Begin Configuration
placeList = [
    "Mahamakut Building",
    "Sara Phra Kaew",
    "CU Sport Complex",
    "Sanum Juub",
    "Samyan Mitr Town"
]

isRun = True

# DB In Format DB[dataID] = dataClass
userDB = {}
placeDB = {}

# End Configuration


class userData:

    def __init__(self):
        self.checkInPlaceID = -1

    def checkIn(self, checkInPlaceID):
        if not (0 <= checkInPlaceID < len(placeList)):
            return

        if self.checkInPlaceID == checkInPlaceID:
            return
        else:
            if (self.checkInPlaceID != -1):
                self.checkOut()
            self.checkInPlaceID = checkInPlaceID
            placeDB[placeList[checkInPlaceID]].addPeople()

    def checkOut(self):
        if (self.checkInPlaceID == -1):
            return
        placeDB[placeList[self.checkInPlaceID]].removePeople()
        self.checkInPlaceID = -1

    def getCurrentCheckInPlaceID(self):
        return self.checkInPlaceID


class placeData:

    def __init__(self):
        self.peopleCount = 0

    def addPeople(self):
        self.peopleCount += 1

    def removePeople(self):
        self.peopleCount -= 1

    def getPeopleCount(self):
        return self.peopleCount


def initialize():
    for place in placeList:
        placeDB[place] = placeData()


def printSeparateLine():
    print("-----------------------------------------------------------------")


def printSeparateText(text):
    printSeparateLine()
    print(text)
    printSeparateLine()


def checkInUser(userPhone, checkInPlaceID):
    outputText = f'Checking in {userPhone} into {placeList[checkInPlaceID]}'

    if (userPhone not in userDB):
        userDB[userPhone] = userData()

    if (userDB[userPhone].getCurrentCheckInPlaceID() == -1):
        userDB[userPhone].checkIn(checkInPlaceID)
        print(outputText)
    elif (userDB[userPhone].getCurrentCheckInPlaceID() == checkInPlaceID):
        print(outputText + " [Already Check In]")
    else:
        previousPlaceID = userDB[userPhone].getCurrentCheckInPlaceID()
        userDB[userPhone].checkIn(checkInPlaceID)
        print(outputText +
              f' [Auto Check Out From {placeList[previousPlaceID]}]')


def checkIn():
    printSeparateLine()
    print("Check in")
    phoneNumber = input("Enter phone number: ")

    while True:
        try:
            for index, place in enumerate(placeList):
                if place in placeDB:
                    print(f'  {index+1}. {place}')
            print("  0. Cancel")
            selectedPlaceID = int(input("Select the place: ")) - 1
            if (selectedPlaceID == -1):
                print("Action Terminated")
                break
            if not (0 <= selectedPlaceID < len(placeList)):
                raise Exception("Invalid Input")
            checkInUser(phoneNumber, selectedPlaceID)
            break
        except:
            printSeparateText("Invalid Input")
            continue
    input("Press Enter To Continue...")
    printSeparateLine()


def checkOutUser(phoneNumber):
    if (phoneNumber not in userDB) or (userDB[phoneNumber].getCurrentCheckInPlaceID() == -1):
        print(f'Cannot Check Out User {phoneNumber}: User Not Check In')
    else:
        previousPlaceID = userDB[phoneNumber].getCurrentCheckInPlaceID()
        userDB[phoneNumber].checkOut()
        print(
            f'Check Out User {phoneNumber} From {placeList[previousPlaceID]}')


def checkOut():
    printSeparateLine()
    print("Check out")
    phoneNumber = input("Enter phone number: ")

    checkOutUser(phoneNumber)
    input("Press Enter To Continue...")
    printSeparateLine()


def printPeopleCount():
    printSeparateLine()
    print("Current Population")
    for index, place in enumerate(placeList):
        if place in placeDB:
            print(f'  {index+1}. {place}: {placeDB[place].getPeopleCount()}')
    input("Press Enter To Continue...")
    printSeparateLine()


def showCurrentCheckInUser():
    printSeparateLine()
    print("Current Check In User")
    for userPhone in userDB:
        userCheckInPlaceID = userDB[userPhone].getCurrentCheckInPlaceID()
        if (userCheckInPlaceID != -1):
            print(
                f'User {userPhone} Currently Check In At: {placeList[userCheckInPlaceID]}')
    input("Press Enter To Continue...")
    printSeparateLine()


def showAllUserInDB():
    printSeparateLine()
    print("All User In DB")
    for userPhone in userDB:
        userCheckInPlaceID = userDB[userPhone].getCurrentCheckInPlaceID()
        if (userCheckInPlaceID != -1):
            print(
                f'User {userPhone} Currently Check In At: {placeList[userCheckInPlaceID]}')
        else:
            print(
                f'User {userPhone} Currently Not Check In')
    input("Press Enter To Continue...")
    printSeparateLine()


def menu():
    global isRun

    while isRun:
        print("""Welcome to Chula Chana!!!
    Available commands:
    1. Check in user
    2. Check out user
    3. Print people count
    4. Show Current Check In User
    5. Show All User In Data Base
    0. Quit""")
        try:
            userSelectOption = int(input("Please input any number: "))
        except:
            printSeparateText("Invalid Input")
            continue

        if (userSelectOption == 0):
            isRun = False
        elif (userSelectOption == 1):
            checkIn()
        elif (userSelectOption == 2):
            checkOut()
        elif (userSelectOption == 3):
            printPeopleCount()
        elif (userSelectOption == 4):
            showCurrentCheckInUser()
        elif (userSelectOption == 5):
            showAllUserInDB()
        else:
            printSeparateText("Option Not Found")


initialize()
menu()
