# Author:   Conrad Berlinguette
# Date:     04 FEB 2020

import os

appName = "GPX Converter"
appVersion = "v1.0"

sourcePath = 'import/'
exportSourcePath = 'export/'
fileList = []


# Functions
#------------------------------------------------------

def getList():
    entries = os.listdir(sourcePath)
    for entry in entries:
        fileList.append(entry)


def printFileList():
    print("Files found:")
    for file in fileList:
        print("-", file)
    print("\n")


def xmlParser(theFile):

    gpxFilePath = os.path.join(sourcePath, theFile)
    gpxFile = open(gpxFilePath, "r")
    gpxFileRead = gpxFile.read()

    newGpxFile = gpxFileRead


    # Extract text
    startText = '<rte>'
    endText = '<desc>'
    extractedText = newGpxFile[newGpxFile.find(startText)+len(startText):newGpxFile.rfind(endText)]


    # Replace text by Position
    startText = 'creator="'
    endText = '" version='
    newText = 'Conrad'
    selectedText = newGpxFile[newGpxFile.find(startText)+len(startText):newGpxFile.find(endText)]
    newGpxFile = newGpxFile.replace(selectedText, newText)


    # Erase text by Exact Match
    newGpxFile = newGpxFile.replace("<desc>", "")
    newGpxFile = newGpxFile.replace("</desc>", "")


    # Insert text
    startText = '<rte>' #start BEFORE this string
    newText = "<metadata></metadata>"
    insertPosition = newGpxFile.find(startText)
    newGpxFile = newGpxFile[:insertPosition] + newText + newGpxFile[insertPosition:]


    # Insert text
    startText = '</metadata>' #start BEFORE this string
    newText = extractedText
    insertPosition = newGpxFile.find(startText)
    newGpxFile = newGpxFile[:insertPosition] + newText + newGpxFile[insertPosition:]


    # Insert text
    startText = '</metadata>' #start BEFORE this string
    newText = "<author>Conrad Berlinguette</author>"
    insertPosition = newGpxFile.find(startText)
    newGpxFile = newGpxFile[:insertPosition] + newText + newGpxFile[insertPosition:]


    # Erase text by Position
    startText = '<rte>'
    endText = '<rtept'
    newText = ''
    selectedText = newGpxFile[newGpxFile.find(startText)+len(startText):newGpxFile.find(endText)]
    newGpxFile = newGpxFile.replace(selectedText, newText)


    # Replace text by Exact Match
    newGpxFile = newGpxFile.replace("rte", "trk")


    # Write the File
    newGpxFilePath = os.path.join(exportSourcePath, theFile)
    f = open(newGpxFilePath, "w")
    f.write(newGpxFile)


    # Close the files
    gpxFile.close()
    f.close()




if __name__ == '__main__':

    # Welcome Text
    print("Welcome to ", appName, appVersion, "\n")

    # List all files in the directory
    getList()
    printFileList()

    # Read File
    for item in fileList:
        xmlParser(item)
