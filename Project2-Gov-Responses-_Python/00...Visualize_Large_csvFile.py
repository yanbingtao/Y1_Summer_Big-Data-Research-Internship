import csv

filePath =r"C:\Users\yanbi\Desktop\Sum_Research2\National data\ALL_National.csv"

###Count rows in the file 
currentFile = open(filePath,"r", encoding="utf8")
rows = 0
for row in currentFile:
    rows += 1

###reopen the file to iterate every rows
currentFile = open(filePath,"r", encoding="utf8")
for i in range(rows):
    currentRow = currentFile.readline()

    ### Use debug to see info via this array
    splitRowInfo=currentRow.split(",")



print("done!")