#! /usr/bin/python3

import time

# Declare Font Character In Global Scope To Reduce Time Complexity
fontCharacter = {}

fontCharacter["0"] = [
    " __ ",
    "|  |",
    "|__|"
]
fontCharacter["1"] = [
    "    ",
    "   |",
    "   |"
]
fontCharacter["2"] = [
    " __ ",
    " __|",
    "|__ "
]
fontCharacter["3"] = [
    " __ ",
    " __|",
    " __|"
]
fontCharacter["4"] = [
    "    ",
    "|__|",
    "   |"
]
fontCharacter["5"] = [
    " __ ",
    "|__ ",
    " __|"
]
fontCharacter["6"] = [
    " __ ",
    "|__ ",
    "|__|"
]
fontCharacter["7"] = [
    " __ ",
    "   |",
    "   |"
]
fontCharacter["8"] = [
    " __ ",
    "|__|",
    "|__|"
]
fontCharacter["9"] = [
    " __ ",
    "|__|",
    " __|"
]
fontCharacter["_"] = [
    "    ",
    "    ",
    " __ "
]


def getFontCharacter(char, line):
    # Input Character And Line Of That Character To Get Character Line String

    if (char in fontCharacter and 0 <= line < len(fontCharacter[char])):
        return fontCharacter[char][line]
    return "    "


def getTimeString(inputData):
    # inputData In Format xx:xx:xx return hour, minute, second string

    # Check Input Type
    if type(inputData) != list:
        return ("__", "__", "__")

    # Check Input Length
    if len(inputData) != 3:
        return ("__", "__", "__")

    # Check Hour, Minute, Second Length
    if (len(inputData[0]) != 2 or
        len(inputData[1]) != 2 or
            len(inputData[2]) != 2):
        return ("__", "__", "__")

    # Check Hour, Minute, Second Is Decimal
    if (not inputData[0].isdecimal() or
        not inputData[1].isdecimal() or
            not inputData[2].isdecimal()):
        return ("__", "__", "__")

    hour, minute, second = inputData

    # Check Minute, Second In Range [0, 59]
    if not (0 <= int(minute) <= 59 and 0 <= int(second) <= 59):
        return ("__", "__", "__")

    return (hour, minute, second)


def timeToSecond(hour, minute, second):
    # Input Hour, Minute, Second In Integer Convert To Second In Integer

    totalMinute = (hour * 60) + minute
    totalSecond = (totalMinute * 60) + second
    return totalSecond


def secondToTime(second):
    # Input Second In Integer Convert To Hour, Minute, Second In Integer

    hour = second // 3600
    second %= 3600
    minute = second // 60
    second %= 60
    return (hour, minute, second)


def printTime(hour, minute, second):
    # Print Output

    print()  # New Line
    for line in range(3):
        hourLineString = f'{getFontCharacter(hour[0], line)} {getFontCharacter(hour[1], line)}'
        minuteLineString = f'{getFontCharacter(minute[0], line)} {getFontCharacter(minute[1], line)}'
        secondLineString = f'{getFontCharacter(second[0], line)} {getFontCharacter(second[1], line)}'
        if (line != 0):
            lineText = f'{hourLineString} · {minuteLineString} · {secondLineString}'
        else:
            lineText = f'{hourLineString}   {minuteLineString}   {secondLineString}'
        print(lineText)


inputData = input("input: ").strip().split(":")
hour, minute, second = getTimeString(inputData)
if ((hour, minute, second) == ("__", "__", "__")):
    # Invalid Format
    printTime(hour, minute, second)
else:
    # Valid Format
    printTime(hour, minute, second)

    # Start Timer
    startTime = time.time()

    # Calculate Total Second
    totalSecond = timeToSecond(int(hour), int(minute), int(second))

    # Calculate Second Left
    secondLeft = totalSecond - int(time.time() - startTime)

    while secondLeft >= 0:
        if (secondToTime(secondLeft) != (int(hour), int(minute), int(second))):
            # If Display Time Update
            hour, minute, second = [str(e).zfill(2)
                                    for e in secondToTime(secondLeft)]
            printTime(hour, minute, second)

        # Reduce CPU Usage
        time.sleep(0.1)

        # Update Second Left
        secondLeft = totalSecond - int(time.time() - startTime)
