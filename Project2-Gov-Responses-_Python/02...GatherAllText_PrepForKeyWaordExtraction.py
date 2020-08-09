import csv
import operator

path=r"C:\Users\yanbi\Desktop\Sum_Research2\RawData"
filePath =path+"\ALL_National.csv"


# position = 12 * (YYYY-2013) + (MM - 1)

##Count rows in the file 
# currentFile = open(filePath,"r", encoding="utf8")
# rows = 0
# for row in currentFile:
#     rows += 1
rows=1359560

currentFile = open(filePath,"r", encoding="utf8")
for i in range(rows):
        currentRow = currentFile.readline()
        splitRowInfo=currentRow.split(",")

        try:
            output=""
            if i==0:
                # do nothing
                a=0
            elif (splitRowInfo[3]==""):
                a=1
            else:
                output=splitRowInfo[0]+splitRowInfo[4]

                output_name=path+"\AllText_ForKeyWordExtract.csv"
                outFile = open(output_name,"a",encoding="utf8")
                outFile.writelines(output)
                outFile.close()
        except:
            continue


print("done!")