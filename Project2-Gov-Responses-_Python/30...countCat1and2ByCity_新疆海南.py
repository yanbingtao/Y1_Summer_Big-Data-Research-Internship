import csv
import operator

prov="新疆维吾尔自治区" #???省辖县(县级市)
citiesInProv=["乌鲁木齐市", "伊犁哈萨克自治州", "克孜勒苏柯尔克孜自治州", "克拉玛依市", "博尔塔拉蒙古自治州", "吐鲁番市", "和田地区", "哈密市", "喀什地区", "塔城地区", "巴音郭楞蒙古自治州", "昌吉回族自治州", "五家渠市","图木舒克市","石河子市","阿拉尔市", "阿克苏地区", "阿勒泰地区"]
# citiesInProv2=["五家渠市","图木舒克市","石河子市","阿拉尔市"]
# prov="海南省"#???省辖县(县级市)
# citiesInProv=["三亚市", "三沙市", "儋州市", "海口市",   "万宁市","东方市","临高县","乐东黎族自治县","五指山市","保亭黎族苗族自治县","定安县","屯昌县","文昌市","昌江黎族自治县","澄迈县","琼中黎族苗族自治县","琼海市","白沙黎族自治县","陵水黎族自治县"]

#
path=r"C:\Users\yanbi\Desktop\Sum_Research2\National data"
filename= path+"\All_"+prov+".csv"


path_out=r"C:\Users\yanbi\Desktop\Sum_Research2\RawData\EachTypeByCity"
output_name= path_out + "\Count_cat_ByCity_include县级市_"+prov+".csv"

cat1_names=["三农","交通","企业", "其他", "医疗","城建","就业", "政务", "教育", "文娱", "旅游", "治安", "环保"]
cat2_names=["两会", "咨询","建言","感谢","投诉","求助"]

##START
### create array to store info
### for assign value: res[row][col]=new value
rows, cols = (len(cat1_names)+len(cat2_names), len(citiesInProv)) 
res = [[0 for i in range(cols)] for j in range(rows)]

# position = 12 * (YYYY-2013) + (MM - 1)
# rows: month date
# col: province

 #Count rows in the file 
currentFile = open(filename,"r", encoding="utf8")
rows = 0
for row in currentFile:
    rows += 1
# rows=1359560


currentFile = open(filename,"r", encoding="utf8")
for row_i in range(rows):
        currentRow = currentFile.readline()
        splitRowInfo=currentRow.split(",")

        try:
            output=""
            if row_i==0:
                # do nothing
                a=0
            else:
                city_str=splitRowInfo[3]
                if (city_str=="省辖县(县级市)"):
                    #for 县级市：
                    city_str=splitRowInfo[4]
                current_cat1_str=splitRowInfo[8]
                current_cat2_str=splitRowInfo[9]

                for city_i in range(int(len(citiesInProv))):
                    if citiesInProv[city_i] == city_str:
                        # if in the same city
                        for cat1_i in range(int(len(cat1_names))):
                            if cat1_names[cat1_i] == current_cat1_str:
                                res[cat1_i][city_i]+=1
                                break
                        for cat2_i in range(int(len(cat2_names))):
                            if cat2_names[cat2_i] == current_cat2_str:
                                res[cat2_i+len(cat1_names)][city_i]+=1
                                break

                        
                        
           
        except:
            continue



###Print out result to file
## Print first row: provinces

# output_name=path+"\2Count_overall"+catName+".csv"

outFile = open(output_name,"a",encoding="utf8")
output=","
# to print the title, citied of the prov
for i in range (len(citiesInProv)):
    output+=citiesInProv[i]+","
output+="\n"
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

    for i in range (len(citiesInProv)):
        output=output+str(res[row_num][i])+","
    output=output+"\n"
    print(output)
    outFile.writelines(output)
    outFile.close()

    row_num+=1

print("done!")