import csv
import operator
import glob

path=r"C:\Users\yanbi\Desktop\Sum_Research2\National data"
fileNameList = glob.glob(path+"/*.csv")
path_out=r"C:\Users\yanbi\Desktop\Sum_Research2\RawData\EachTypeByCity"
output_name= path_out + "\Count_catByProv.csv"
# catName="供暖"
cat1_names=["三农","交通","企业", "其他", "医疗","城建","就业", "政务", "教育", "文娱", "旅游", "治安", "环保"]
cat2_names=["两会", "咨询","建言","感谢","投诉","求助"]

##START
### create array to store info
### for assign value: res[row][col]=new value
rows, cols = (len(cat1_names)+len(cat2_names), len(fileNameList)) 
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
                else:
                    current_cat1_str=splitRowInfo[8]
                    current_cat2_str=splitRowInfo[9]

                    for cat1_i in range(int(len(cat1_names))):
                        if cat1_names[cat1_i] == current_cat1_str:
                            res[cat1_i][province_count]+=1
                    for cat2_i in range(int(len(cat2_names))):
                        if cat2_names[cat2_i] == current_cat2_str:
                            res[cat2_i+len(cat1_names)][province_count]+=1
            except:
                continue
    province_count+=1



###Print out result to file
## Print first row: provinces

# output_name=path+"\2Count_overall"+catName+".csv"

outFile = open(output_name,"a",encoding="utf8")
output="Provinces:,上海市,云南省,内蒙古,北京市,吉林省,四川省,天津市,宁夏回族自治区,安徽省,山东省,山西省,山西省_updated,广东省,广西省,新疆维吾尔自治区,江苏省,江西省,河北省,河北省_updated,河南省,浙江省,海南省,湖北省,湖南省,澳门特别行政区,甘肃省,福建省,西藏自治区,贵州省,辽宁省,重庆市,陕西省,青海省,香港特别行政,黑龙江"+"\n"
outFile.writelines(output)
outFile.close()


row_num=0;
for row in res: 
    if row_num<len(cat1_names):
        output="Cat1"+cat1_names[row_num]
    else:
        output="Cat2"+cat2_names[row_num-len(cat1_names)]

        
    # print(str(yyyy),str(mm),":",row)

    outFile = open(output_name,"a",encoding="utf8")
    output=output+","

    for i in range (len(fileNameList)):
        output=output+str(res[row_num][i])+","
    output=output+"\n"
    print(output)
    outFile.writelines(output)
    outFile.close()

    row_num+=1

print("done!")