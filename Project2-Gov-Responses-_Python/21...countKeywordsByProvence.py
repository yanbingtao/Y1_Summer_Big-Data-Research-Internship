import csv
import operator
import glob

path=r"C:\Users\yanbi\Desktop\Sum_Research2\National data"
fileNameList = glob.glob(path+"/*.csv")

keyWord_cat="工程建设"
keywords=['开发商','拆迁','施工','改造','建设','规划','违建','搬迁','拆除','危房','棚户区']

# keyWord_cat="一号工程"
# keywords=['扶贫','低保','扶贫','宅基地','三农','农村','农业','农民','农民工','贫困户','脱贫','一号工程']

# keyWord_cat="环保"
# keywords=['环境', '垃圾', '污染',  '绿化', '污水', '油烟','脏乱差', '清理', '绿地', '环保局', '霾', '尾气']

# keyWord_cat="招商引资"
# keywords=['项目','发展','新区','企业','贷款','开发区','集团','招商','引资']

path_out=r"C:\Users\yanbi\Desktop\Sum_Research2\RawData\EachTypeByProv"
output_name= path_out + "\Count_keyWord"+keyWord_cat+"ByProv_updated.csv"

# cat1_names=["三农","交通","企业", "其他", "医疗","城建","就业", "政务", "教育", "文娱", "旅游", "治安", "环保"]
# cat2_names=["两会", "咨询","建言","感谢","投诉","求助"]

##START
### create array to store info
### for assign value: res[row][col]=new value
rows, cols = (1, len(fileNameList)) 
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
                    title_str=splitRowInfo[6]
                    content_str=splitRowInfo[11]
                    for keyword in keywords:
                        b1=title_str.find(keyword)
                        b2=content_str.find(keyword)
                        if (b1>=0 or b2>=0):
                            res[0][province_count]+=1
            except:
                continue
    province_count+=1



###Print out result to file
## Print first row: provinces

# output_name=path+"\2Count_overall"+catName+".csv"

outFile = open(output_name,"a",encoding="utf8")
output="Provinces:,上海市,云南省,内蒙古,北京市,吉林省,四川省,天津市,宁夏回族自治区,安徽省,山东省,山西省,山西省_updated,广东省,广西省,新疆维吾尔自治区,江苏省,江西省,河北省,河北省_updated,河南省,浙江省,海南省,湖北省,湖南省,澳门特别行政区,甘肃省,福建省,西藏自治区,贵州省,辽宁省,重庆市,陕西省,青海省,香港特别行政区,黑龙江"+"\n"
outFile.writelines(output)
outFile.close()


row_num=0;
for row in res: 
    
    output="KeywordCat "+keyWord_cat

        
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