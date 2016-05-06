
####################################
# File name: ClearProject.py       #
# Author: AhMeDz                   #
# Submission:  5 May 2016          #
####################################

"""CleanProject.py: Deletes unused image drawables from given project directory"""

import os, re, sys, webbrowser

whiteList = set()
regexList = set()
outputFile = "output.txt"
f = open(outputFile, 'w')
deletedFiles = 0
bytesFreed = 0

#Check whether given directory holds drawables or not.
def isResourceDir(directory):
  return (
  (os.path.exists(directory+"/drawable"))        or
  (os.path.exists(directory+"/drawable-ldpi"))   or
  (os.path.exists(directory+"/drawable-mdpi"))   or
  (os.path.exists(directory+"/drawable-hdpi"))   or
  (os.path.exists(directory+"/drawable-xhdpi"))  or
  (os.path.exists(directory+"/drawable-xxhdpi")) or
  (os.path.exists(directory+"/drawable-xxxhdpi"))) and "src" in directory

#We only want to remove unused PICTURES (pngs)
def addFileToWhiteList(fileName):
  #United scheme for later processing
  fileName = fileName.replace("R.drawable.", "").replace("@drawable/","")
  whiteList.add(fileName)

#Find pattern in string and return list of matches.
def findAll(regex, content):
  pattern = re.compile(regex)
  return pattern.findall(content)

#Check to see what resources are referenced in this function.
def checkFileForResources(path):
  file = open(path, 'r')
  contents = file.read()
  file.close()

  #Search code files.
  results = findAll('R.drawable.[a-zA-Z0-9_]*', contents)
  for result in results:
    addFileToWhiteList(result)

  #Search layout files.
  results = findAll('@drawable/[a-zA-Z0-9_]*', contents)
  for result in results:
    addFileToWhiteList(result)

#Get file size by path
def getFileSize(path):
  return os.path.getsize(path) / 1024.0 / 1024.0

#Check if fileName matches any given regex or not.
def matchRegex(fileName):
  for regex in regexList:
    if len(findAll(regex, fileName)) > 0:
      # print fileName, " matches ", regex
      return True

  return False


#We only want to if it's an unreferenced PNG.
def deleteIfUnused(directory, origFileName):
    if origFileName.endswith(".png"):
      fileName = os.path.splitext(origFileName)[0]
      if fileName.endswith(".9.png"):
        fileName = os.path.splitext(fileName)[0]
      #Delete if not whiteListed nor matches any given Regex.
      if fileName not in whiteList:
        if matchRegex(fileName):
          addFileToWhiteList(fileName)
        else:
          deleteResFile(directory, origFileName)

#Delete file and update status.
def deleteResFile(directory, fileName):
  #Do stats tracking.
  global deletedFiles
  global bytesFreed
  path = directory+"/"+fileName
  deletedFiles += 1
  fileSize = getFileSize(path)
  bytesFreed += fileSize

  #Actually delete the file.
  os.unlink(path)
  printToFile(("Deleted (%.4f Mbs): " + path) % fileSize)

#Print to file.
def printToFile(s):
  # print s
  f.write(s + "\n")

#Shows status of completion.
def showStatus():
  if len(whiteList) != 0: 
    printToFile("")
    printToFile("files that has been excluded.")

  for fileName in whiteList:
    printToFile(fileName)

  printToFile("")
  printToFile("%d file(s) deleted" % deletedFiles)
  printToFile("%.4f Mbs were freed" % bytesFreed)

  #Open file using the browser library (actually will open it in the default OS app for text files).
  f.close()
  print ("Opening output file.")
  webbrowser.open(outputFile)
  print ("Done!")

#######################################################################

#Make sure the arguements are provided correctly (at least the project's path)
args = sys.argv
if len(args) < 2:
  print "Type: python CleanProject.py \'directory_path\' + any number of expressions space separated."
  quit()

rootDir = args[1]
resDir = rootDir

#Rest of the arguements are probably the expressions to exclude.
for i in range(2,len(args)):
  regexList.add(args[i])

#Detect the resources folder and whiteList the files used in project.
for root, dirs, files in os.walk(rootDir):
  if isResourceDir(root):
    resDir = root

  for file in files:
    checkFileForResources(root+"/"+file)

print ("Detected resource directory: %s" % resDir)

for root, dirs, files in os.walk(resDir):
    for file in files:
      deleteIfUnused(root, file)

showStatus()
