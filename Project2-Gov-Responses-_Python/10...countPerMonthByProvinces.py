import csv
import operator
import glob

path=r"C:\Users\yanbi\Desktop\Sum_Research2\National data"
fileNameList = glob.glob(path+"/*.csv")
# catName="供暖"


### create array to store info
### for assign value: res[row][col]=new value
rows, cols = (96, len(fileNameList)) 
res = [[0 for i in range(cols)] for j in range(rows)]

# position = 12 * (YYYY-2013) + (MM - 1)
# rows: month date
# col: province


province_count=0
for file in fileNameList:

    #Count rows in the file 
    currentFile = open(file,"r", encoding="utf8")
    rows = 0
    for row in currentFile:
        rows += 1
    # rows=1359560

    currentFile = open(file,"r", encoding="utf8")
    for i in range(rows):
            currentRow = currentFile.readline()
            splitRowInfo=currentRow.split(",")

            try:
                output=""
                if i==0:
                    # do nothing
                    a=0
                elif (splitRowInfo[10]==""):
                    a=1
                else:
                    timeInput=splitRowInfo[10]
                    yyyy=timeInput[0:4]
                    mm=timeInput[5:7]
                    pos_month=12 * (int(yyyy)-2013) + (int(mm) - 1)
                # same cat？
                    # if splitRowInfo[2]==catName:
                    #     res[pos]=res[pos]+1
                # contain keyword？
                    # if ((splitRowInfo[0]).find(catName) or (splitRowInfo[4]).find(catName)):
                        # res[pos]=res[pos]+1
                # overall, without cat and keywords
                res[pos_month][province_count]+=1
            except:
                continue
    province_count+=1



###Print out result to file
## Print first row: provinces

# output_name=path+"\2Count_overall"+catName+".csv"
output_name= path + "\Count2_overall.csv"
outFile = open(output_name,"a",encoding="utf8")
output="Provinces:,上海市，云南省，内蒙古，北京市，吉林省，四川省，天津市，宁夏回族自治区，安徽省，山东省，山西省，广东省，广西省，新疆维吾尔自治区，江苏省，江西省，河北省，河南省，浙江省，海南省，湖北省，湖南省，澳门特别行政区，甘肃省，福建省，西藏自治区，贵州省，辽宁省，重庆市，陕西省，青海省，香港特别行政，"+"\n"
outFile.writelines(output)
outFile.close()


row_num=0;
for row in res: 
    ### calculate month in YYYYMM
    yyyy=str(int(row_num/12+2013))
    mm=str((row_num%12)+1).zfill(2)
    print(str(yyyy),str(mm),":",row)

    outFile = open(output_name,"a",encoding="utf8")
    output=(yyyy)+"-"+(mm)+"," #+str(row)+"\n"
    for i in range (len(fileNameList)):
        output=output+str(res[row_num][i])+","
    output=output+"\n"
    outFile.writelines(output)
    outFile.close()

    row_num+=1

print("done!")