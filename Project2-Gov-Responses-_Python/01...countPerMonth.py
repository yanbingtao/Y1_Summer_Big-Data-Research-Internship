import csv
import operator

path=r"C:\Users\yanbi\Desktop\Sum_Research2\RawData"
filePath =path+"\ALL_National.csv"
# path=r"C:\Users\yanbi\Desktop\Sum_Research2\National data"
# filePath =path+"\All_安徽省.csv"
catName="供暖"

res=[0]*96
for i in range (96):
    res[0]=0

# position = 12 * (YYYY-2013) + (MM - 1)

#Count rows in the file 
currentFile = open(filePath,"r", encoding="utf8")
rows = 0
for row in currentFile:
    rows += 1
# rows=1359560

currentFile = open(filePath,"r", encoding="utf8")
for i in range(rows):
        currentRow = currentFile.readline()
        splitRowInfo=currentRow.split(",")

        try:
            output=""
            # if i==0:
            #     # do nothing
            #     a=0
            # el
            if (splitRowInfo[3]==""):
                a=1
            else:
                timeInput=splitRowInfo[3]
                yyyy=timeInput[0:4]
                mm=timeInput[4:6]
                # mm=timeInput[5:7]
                pos=12 * (int(yyyy)-2013) + (int(mm) - 1)
            # # same cat？
                # if splitRowInfo[8]==catName:
                #     res[pos]=res[pos]+1
            # contain keyword？
                b0=(splitRowInfo[0]).find(catName)
                b1=(splitRowInfo[4]).find(catName)
                #==0:contain: ==-1:not contain
                if (b0==0 or b1==0):
                    res[pos]=res[pos]+1
        except:
            continue

flag=0;
for row in res: 
    ### calculate month in YYYYMM
    yyyy=str(int(flag/12+2013))
    mm=str((flag%12)+1).zfill(2)
    flag+=1
    print(str(yyyy),str(mm),":",row)

    outpath=r"C:\Users\yanbi\Desktop\Sum_Research2\RawData\Task1"
    output_name=outpath+"\Count_全国_KeyWord"+catName+".csv"
    outFile = open(output_name,"a",encoding="utf8")
    output=(yyyy)+"-"+(mm)+","+str(row)+"\n"
    outFile.writelines(output)
    outFile.close()

print("done!")