import csv
import operator
import math as math
import datetime

path=r"C:\Users\yanbi\Desktop\Sum_Research3\RawData\ChangeWeekNumToData"
filename = path+"\PostDataBalancedPanel_byCity.csv"
# start from 1
rowsNoCount=2
weekNumCol=3

path_out=r"C:\Users\yanbi\Desktop\Sum_Research3\RawData\ChangeWeekNumToData"
output_name= path_out + "\BalancedPanel11111.csv"

##START

#Count rows in the file 
currentFile = open(filename,"r", encoding="utf8")
rows = 0
for row in currentFile:
    rows += 1


currentFile = open(filename,"r", encoding="utf8")
for row_i in range(rows):
    output=""
    if row_i<rowsNoCount:
        # copy paste all text
        currentRow = currentFile.readline()
        output=","+currentRow
    else:
        currentRow = currentFile.readline()
        splitRowInfo=currentRow.split(",")

        # try:
        weekNum_str=splitRowInfo[weekNumCol-1]

        d1=str(weekNum_str[1:5])
        d2="-W"
        d3=str(weekNum_str[10:len(weekNum_str)])
        d=d1+d2+d3
        r=str(datetime.datetime.strptime(d+'-1','%G-W%V-%u'))
        updatedWeekNum_str=r[0:10]

        output=""
        for update_i in range (len(splitRowInfo)):
            if (update_i!=weekNumCol-1):
                output+=splitRowInfo[update_i]+","
            else:
                output+=splitRowInfo[update_i]+","+updatedWeekNum_str+","
        # except:
        #     continue

    ###Print out result to file
    ## Print first row: city
    outFile = open(output_name,"a",encoding="utf8")
    # if row_i>=rowsNoCount:
    #     output+="\n"
    outFile.writelines(output)
    outFile.close()
 
print(str(filename)+": done!")