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

# Get the log file names and paths
filesPaths = [] # a list of all the paths
filesNames = [] # a list of all the file names
for root,dirs,files in os.walk(folderPath): # get log file names
    for file in files:
        if file.endswith(".log") or file.endswith(".txt"):
            filesPaths.extend([file])
            filesNames.extend([file])

# Making "filesPaths" contains the full address of each log file
y = 0
for x in filesPaths:
    x = folderPath+"\\"+x
    filesPaths[y] = x
    y = y+1

# Count the number of times the string appears in the logs
finalList = [] # the final list with all the results
for x in range(len(filesPaths)):
    for y in range(len(arrayOfStrings)):
        with open(filesPaths[x], 'r') as file:
            data = file.read().replace('\n', '')
            numberOfTimes = data.count(arrayOfStrings[y])
            finalList.extend([[filesNames[x], arrayOfStrings[y], numberOfTimes]])

# Sort the final list, based on the count number
finalList = sorted(finalList, key=itemgetter(2,2),reverse=True)

# Make a new list from the final list, that includes "a href" html tags
finalListWithLinks = finalList
for x in range (len(finalList)):
    finalListWithLinks[x][0] = "<a href=\""+folderPath+"//"+finalList[x][0]+"\">"+finalList[x][0]+"</a>"

# Create html report
fileName = folderPath+"\\report.html"
f = open(fileName, "w")
f.write(tabulate(finalListWithLinks, tablefmt='html',headers=["File Name","String", "Count"]))
f.close()

# Create links from file names
with open(fileName, 'r') as file :
    filedata = file.read()
filedata = filedata.replace('&lt;', '<')
filedata = filedata.replace('&quot;', '"')
filedata = filedata.replace('&gt;', '>')
with open(fileName, 'w') as file:
    file.write(filedata)
    
print("Done!")
