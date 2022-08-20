import os
from tabulate import tabulate
from operator import itemgetter

# Creates an array from a string
def transformToArray(array):
    y = 0
    newArray = [""]
    for x in array:
        if x == ' ':
            y = y + 1
            newArray.extend([""])
            continue
        newArray[y] = newArray[y] + x
    return newArray

# Take input from the user + transform the string to an array
arrayOfStrings = input("Please enter an array of strings: (separate each word with a space) ")
folderPath = input("Please enter a folder path: ")
arrayOfStrings = transformToArray(arrayOfStrings)
print(arrayOfStrings)

# Get the log file names and paths
filesPaths = [] # a list of all the paths
filesNames = [] # a list of all the file names
for root,dirs,files in os.walk(folderPath): # get log file names
    for file in files:
        if file.endswith(".log") or file.endswith(".txt"):
            filesPaths.extend([file])
            filesNames.extend([file])
print(filesPaths)

# Making "filesPaths" contains the full address of each log file
y = 0
for x in filesPaths:
    x = folderPath+"\\"+x
    print(x)
    filesPaths[y] = x
    print(filesPaths[y])
    y = y+1

print()
# Count the number of times the string appears in the logs
finalList = [] # the final list with all the results
for x in range(len(filesPaths)):
    for y in range(len(arrayOfStrings)):
        with open(filesPaths[x], 'r') as file:
            data = file.read().replace('\n', '')
            numberOfTimes = data.count(arrayOfStrings[y])
            finalList.extend([[filesNames[x], arrayOfStrings[y], numberOfTimes]])
print(finalList)

# Sort the final list, based on the count number
print(sorted(finalList, key=itemgetter(2,2),reverse=True))
finalList = sorted(finalList, key=itemgetter(2,2),reverse=True)

# Create html report
f = open(folderPath+"\\report.html", "w")
f.write(tabulate(finalList, tablefmt='html',headers=["File Name","String", "Count"]))
f.close()
