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


path_out=r"C:\Users\yanbi\Desktop\Sum_Research2\RawData\ReplyTimeByCity"
output_name= path_out + "\getPosttimeNReplytime_ByCity_include县级市"+prov+".csv"


##START
### create array to store info
### for assign value: res[row][col]=new value
rows, cols = (2, len(citiesInProv)) 
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

                #check point
                if city_str=="舟山市":
                    a=0

                post_time_str=int(splitRowInfo[10][0:4]+splitRowInfo[10][5:7]+splitRowInfo[10][8:10])
                for city_i in range(int(len(citiesInProv))):
                    if citiesInProv[city_i] == city_str:
                        # if in the same city
                        if res[0][city_i] == 0:
                            res[0][city_i]=post_time_str
                        elif post_time_str<res[0][city_i]:
                            res[0][city_i]=post_time_str

                if (splitRowInfo[14][0]=='2'):
                    reply_time_str=int(splitRowInfo[14][0:4]+splitRowInfo[14][5:7]+splitRowInfo[14][8:10])  
                elif (splitRowInfo[15][0]=='2'):
                    reply_time_str=int(splitRowInfo[15][0:4]+splitRowInfo[15][5:7]+splitRowInfo[15][8:10])
                elif (splitRowInfo[16][0]=='2'):
                    reply_time_str=int(splitRowInfo[16][0:4]+splitRowInfo[16][5:7]+splitRowInfo[16][8:10])
                elif (splitRowInfo[17][0]=='2'):
                    reply_time_str=int(splitRowInfo[17][0:4]+splitRowInfo[17][5:7]+splitRowInfo[17][8:10])

                for city_i in range(int(len(citiesInProv))):
                    if citiesInProv[city_i] == city_str:
                        # if in the same city
                        if res[1][city_i] == 0:
                                res[1][city_i]=post_time_str
                        elif post_time_str<res[1][city_i]:
                            res[1][city_i]=post_time_str

                        
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
    if row_num==0:
        output="Post Time:"
    else:
        output="Reply Time:"

        
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