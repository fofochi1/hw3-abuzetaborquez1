#problem 1
import string


def stringChecker():
    word = input('What is the string: ')
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowelsCounter = 0
    consonantsCounter = 0
    for x in word:
        if x in vowels:
            vowelsCounter += 1
        elif x != ' ':
            consonantsCounter += 1
    if vowelsCounter > consonantsCounter:
        return True
    elif vowelsCounter < consonantsCounter:
        return False
    elif vowelsCounter == consonantsCounter:
        return None
stringChecker()

#problem 2
import math
def findVolume():
    R = input('Enter Radius: ')
    H = input('Enter height: ')
    volume = math.pi*(R*R)*H
    return volume
findVolume()

#problem 3
def csv(inputStr):
    #inputStr = input('enter list: ')
    strList = inputStr.split()
    csvString = ",".join(strList)
    return csvString


#problem 4
def outputIntoFile(listsOfString):
    length = len(listsOfString)
    for i in range(length):
        csvString = csv(listsOfString[i])
        f = open("csvFile.txt", 'a')
        f.write(csvString + "\n")
        f.close()
        print(csvString)

outputIntoFile(['hello how are you', 'nice to meet you'])

#problem 5
def changeCSV(fileName):
    f = open(fileName, 'r')
    lines = f.readlines()
    print(lines)

changeCSV('csvFile.txt')

#problem 6
def catchZero(num1, num2):
    try:
        num1/num2
    except ZeroDivisionError:
        print('Cannot divide by zero')

catchZero(3,0)

#problem 7
def removeDuplicates(numberList):
    nonDuplicates = list(set(numberList))
    print(nonDuplicates)

removeDuplicates([1,2,3,3,4,5,6,6,7,8,8])

#problem 8
import os
def createDirectory():
    path = os.getcwd()
    os.mkdir(path + "/softwareEngineer/hw3/hw3-folder")

createDirectory()