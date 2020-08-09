import csv
import operator

path=r"C:\Users\yanbi\Desktop\Sum_Research2\National data"
filePath =path+"\ALL_National.csv"

###Count rows in the file 
# currentFile = open(filePath,"r", encoding="utf8")
# rows = 0
# for row in currentFile:
#     rows += 1

###reopen the file to iterate every rows
currentFile = open(filePath,"r", encoding="utf8")
csv1=csv.reader(currentFile,delimiter=",")
sort = sorted(csv1,key=operator.itemgetter(3))

### Print in a new file
output_name=path+"\ALL_National_Sorted.csv"
outFile = open(output_name,"a",encoding="utf8")
outFile.writelines(sort)
outFile.close()


print("done!")