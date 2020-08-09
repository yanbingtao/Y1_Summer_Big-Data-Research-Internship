import csv
import operator
import math as math
import datetime
import glob

path=r"C:\Users\yanbi\Desktop\Sum_Research3\National data"
# filename= path+"\All_"+prov+".csv"
fileNameList = glob.glob(path+"/*.csv")

# provs=["云南省","内蒙古","吉林省","四川省","宁夏回族自治区","安徽省","山东省","山西省","广东省","广西省","江苏省","江西省","河北省","河南省","浙江省","湖北省","湖南省","甘肃省","福建省","西藏自治区","贵州省","辽宁省","陕西省","青海省","黑龙江省"]

prov="云南省"
citiesInProv=["云南省"]
fileNameList = [path+'\历史天气_5.csv',path+'\历史天气_14.csv',path+'\历史天气_15.csv']
# prov="内蒙古"
# citiesInProv=["内蒙古"]
# fileNameList = [path+'\历史天气_4.csv',path+'\历史天气_10.csv',path+'\历史天气_11.csv']
# prov="吉林省"
# citiesInProv=["吉林省"]
# fileNameList = [path+'\历史天气_3.csv',path+'\历史天气_4.csv',path+'\历史天气_10.csv']
# prov="四川省"
# citiesInProv=["四川省"]
# fileNameList = [path+'\历史天气_5.csv',path+'\历史天气_6.csv',path+'\历史天气_13.csv']
# prov="宁夏回族自治区"
# citiesInProv=["宁夏回族自治区"]
# fileNameList = [path+'\历史天气_4.csv',path+'\历史天气_11.csv']
# prov="安徽省"
# citiesInProv=["安徽省"]
# fileNameList = [path+'\历史天气_0.csv']
# prov="山东省"
# citiesInProv=["山东省"]
# fileNameList = [path+'\历史天气_4.csv',path+'\历史天气_5.csv',path+'\历史天气_11.csv',path+'\历史天气_12.csv']
# prov="山西省"
# citiesInProv=["山西省"]
# fileNameList = [path+'\历史天气_5.csv',path+'\历史天气_12.csv',path+'\历史天气_13.csv']
# prov="广东省"
# citiesInProv=["广东省"]
# fileNameList = [path+'\历史天气_0.csv',path+'\历史天气_1.csv',path+'\历史天气_3.csv',path+'\历史天气_4.csv']
# prov="广西省"
# citiesInProv=["广西省"]
# fileNameList = [path+'\历史天气_1.csv',path+'\历史天气_4.csv',path+'\历史天气_5.csv',path+'\历史天气_6.csv']
# prov="江苏省"
# citiesInProv=["江苏省"]
# fileNameList = [path+'\历史天气_3.csv',path+'\历史天气_9.csv']
# prov="江西省"
# citiesInProv=["江西省"]
# fileNameList = [path+'\历史天气_3.csv',path+'\历史天气_9.csv',path+'\历史天气_10.csv']
# prov="河北省"
# citiesInProv=["河北省"]
# fileNameList = [path+'\历史天气_2.csv',path+'\历史天气_7.csv',path+'\历史天气_8.csv']
# prov="河南省"
# citiesInProv=["河南省"]
# fileNameList = [path+'\历史天气_2.csv',path+'\历史天气_3.csv',path+'\历史天气_8.csv']
# prov="浙江省"
# citiesInProv=["浙江省"]
# fileNameList = [path+'\历史天气_6.csv',path+'\历史天气_7.csv',path+'\历史天气_15.csv']
# prov="湖北省"
# citiesInProv=["湖北省"]
# fileNameList = [path+'\历史天气_2.csv',path+'\历史天气_3.csv',path+'\历史天气_8.csv',path+'\历史天气_9.csv']
# prov="湖南省"
# citiesInProv=["湖南省"]
# fileNameList = [path+'\历史天气_7.csv',path+'\历史天气_15.csv',path+'\历史天气_16.csv']
# prov="甘肃省"
# citiesInProv=["甘肃省"]
# fileNameList = [path+'\历史天气_0.csv',path+'\历史天气_2.csv',path+'\历史天气_3.csv']
# prov="福建省"
# citiesInProv=["福建省"]
# fileNameList = [path+'\历史天气_0.csv',path+'\历史天气_1.csv',path+'\历史天气_2.csv']
# prov="西藏自治区"
# citiesInProv=["西藏自治区"]
# fileNameList = [path+'\历史天气_6.csv',path+'\历史天气_14.csv']
# prov="贵州省"
# citiesInProv=["贵州省"]
# fileNameList = [path+'\历史天气_1.csv',path+'\历史天气_2.csv',path+'\历史天气_6.csv',path+'\历史天气_7.csv']
# prov="辽宁省"
# citiesInProv=["辽宁省"]
# fileNameList = [path+'\历史天气_3.csv',path+'\历史天气_4.csv',path+'\历史天气_10.csv']
# prov="陕西省"
# citiesInProv=["陕西省"]
# fileNameList = [path+'\历史天气_7.csv',path+'\历史天气_16.csv']
# prov="青海省"
# citiesInProv=["青海省"]
# fileNameList = [path+'\历史天气_4.csv',path+'\历史天气_11.csv']
# prov="黑龙江省"
# citiesInProv=["黑龙江省"]
# fileNameList = [path+'\历史天气_2.csv',path+'\历史天气_8.csv']
#





path_out=r"C:\Users\yanbi\Desktop\Sum_Research3\RawData"
output_name= path_out + "\BalancedPanel_byProv_"+prov+".csv"

##START
### create array to store info
### for assign value: res[row][col]=new value
### 53 week per year, 2011~2019: total 9; 9*52=468; +begin+end=470; +2015:53th week=471
rows, cols = (8, len(citiesInProv)*471) 
res = [[0 for i in range(cols)] for j in range(rows)]
res_count = [[0 for i in range(cols)] for j in range(rows)]

# position = 12 * (YYYY-2013) + (MM - 1)
# rows: month date
# col: province

for filename in fileNameList: 
    #Count rows in the file 
    currentFile = open(filename,"r", encoding="utf8")
    rows = 0
    for row in currentFile:
        rows += 1


    currentFile = open(filename,"r", encoding="utf8")
    for row_i in range(rows):
            currentRow = currentFile.readline()
            splitRowInfo=currentRow.split(",")

            try:
                output=""
                
                prov_str=splitRowInfo[0]
                city_str=splitRowInfo[1]

                AQI_str=splitRowInfo[9]
                
                time_str=splitRowInfo[3]
                if len(time_str)==9:
                    time_str_int=int(time_str[0:1]+time_str[2:4]+time_str[5:9])
                    time_yyyy_str=int(time_str[5:9])
                    time_mm_str=int(time_str[2:4])
                    time_dd_str=int(time_str[0:1])
                elif len(time_str)==10:
                    time_str_int=int(time_str[0:2]+time_str[3:5]+time_str[6:10])
                    time_yyyy_str=int(time_str[6:10])
                    time_mm_str=int(time_str[3:5])
                    time_dd_str=int(time_str[0:2])

            
                #to decide which week for post time
                #(2011, 52, 6) or 201101
                time_week=-1
                time_week_yyyy=datetime.date(time_yyyy_str,time_mm_str,time_dd_str).isocalendar()[0]
                time_week_mm=datetime.date(time_yyyy_str,time_mm_str,time_dd_str).isocalendar()[1]
                #dd: 1~7; Not 0~6
                time_week_dd=datetime.date(time_yyyy_str,time_mm_str,time_dd_str).isocalendar()[2]
                if time_week_yyyy==2010 and time_str_int>=20110101:
                    time_week=0
                elif time_week_yyyy<=2015:
                    time_week=(time_week_yyyy-2011)*52+time_week_mm
                elif time_week_yyyy>2015 and time_week_yyyy<=2019:
                    time_week=(time_week_yyyy-2011)*52+1+time_week_mm
                elif time_week_yyyy==2020 and time_str_int<20200101:
                    time_week=470

                # for AQI
                Row=0
                Col=0
                for city_i in range(int(len(citiesInProv))):
                    prov_partial=str(prov)[0:2]#eg 安徽省-> 安徽
                    b_prov1=prov_str.find(prov_partial)
                    b_prov2=str(prov)[0:2].find(prov_str)
                    if b_prov1>=0 or b_prov2>=0:
                        # if in the same prov
                        # city_partial=citiesInProv[city_i][0:len(citiesInProv[city_i])-1]#eg 合肥市-> 合肥
                        # b_city1=city_str.find(city_partial)
                        # b_city2=citiesInProv[city_i].find(city_str)
                        # if b_city1>=0 or b_city2>=0:
                            # if in the same city
                            if time_week>=0:
                                # check which day(row) to put AQI in
                                Row=time_week_dd-1
                                Col=city_i*471+time_week

                                if (AQI_str!=''):
                                    res_count[Row][Col]+=1
                                    sumTemp=(res[Row][Col]+int(AQI_str))
                                    res[Row][Col]=sumTemp
                                    break
            except:
                continue

###Calculate average AQI for each day, each week for each city


for aveAQI_i in range (cols):

    sum=0
    for ave_row_i in range (7):
        if res_count[ave_row_i][aveAQI_i]==0:
            res_count[ave_row_i][aveAQI_i]=1
        res[ave_row_i][aveAQI_i]=res[ave_row_i][aveAQI_i]/res_count[ave_row_i][aveAQI_i]
        rrr=res[ave_row_i][aveAQI_i]
        sum+=res[ave_row_i][aveAQI_i]
    res[7][aveAQI_i]=sum/7


###Print out result to file
## Print first row: city
outFile = open(output_name,"a",encoding="utf8")
output=","
for i in range (len(citiesInProv)):
    for j in range (471):
        output+=citiesInProv[i]+","
output+="\n"
outFile.writelines(output)
outFile.close()
 
## Print 2nd row: week number
outFile = open(output_name,"a",encoding="utf8")
output=","
for i in range (len(citiesInProv)):
    for j in range (471):
        if j==0:
            output+="Y2010 Week52"+","
        elif j==471:
            output+="Y2020 Week1"+","
        elif j ==261:
            output+="Y2015 Week53"+","
        elif j<261:
            #y2011~y2015dec31
            year=math.ceil(j/52)+2010
            week=j-(math.ceil(j/52)-1)*52
            output+="Y"+str(year)+" Week"+str(week)+","
        elif j>261:
            year=math.ceil((j-1)/52)+2010
            week=j-(math.ceil((j-1)/52)-1)*52-1
            output+="Y"+str(year)+" Week"+str(week)+","
            # output+="Week "+str(j)+","
output+="\n"
outFile.writelines(output)
outFile.close()

## Print res array data
row_num=0;
for row in res: 
    if row_num==0:
        output="Day1 City-Level Ave AQI,"
    elif row_num==1:
        output="Day2 City-Level Ave AQI,"
    elif row_num==2:
        output="Day3 City-Level Ave AQI,"
    elif row_num==3:
        output="Day4 City-Level Ave AQI,"
    elif row_num==4:
        output="Day5 City-Level Ave AQI,"
    elif row_num==5:
        output="Day6 City-Level Ave AQI,"
    elif row_num==6:
        output="Day7 City-Level Ave AQI,"
    elif row_num==7:
        output="Weekly City-Level Ave AQI,"

    outFile = open(output_name,"a",encoding="utf8")

    for i in range (len(citiesInProv)*471):
        output=output+str(res[row_num][i])+","
    output=output+"\n"
    # print(output)
    outFile.writelines(output)
    outFile.close()

    row_num+=1

print(prov+"done!")