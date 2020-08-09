import csv
import operator
import math as math
import datetime

prov="上海市"
# prov="北京市"
# prov="天津市"
# prov="澳门特别行政区"
# prov="重庆市"
# prov="香港特别行政区"
#
keyWord_cat0="工程建设"
keywords0=['开发商','拆迁','施工','改造','建设','规划','违建','搬迁','拆除','危房','棚户区']

keyWord_cat1="一号工程"
keywords1=['扶贫','低保','扶贫','宅基地','三农','农村','农业','农民','农民工','贫困户','脱贫','一号工程']

keyWord_cat2="环保"
keywords2=['环境', '垃圾', '污染',  '绿化', '污水', '油烟','脏乱差', '清理', '绿地', '环保局', '霾', '尾气']

keyWord_cat3="招商引资"
keywords3=['项目','发展','新区','企业','贷款','开发区','集团','招商','引资']

#
cat1_names=["三农","交通","企业", "其他", "医疗","城建","就业", "政务", "教育", "文娱", "旅游", "治安", "环保"]
cat2_names=["两会", "咨询","建言","感谢","投诉","求助"]
#


path=r"C:\Users\yanbi\Desktop\Sum_Research2\National data"
filename= path+"\All_"+prov+".csv"


path_out=r"C:\Users\yanbi\Desktop\Sum_Research2\RawData\BalancedPanel"
output_name= path_out + "\BalancedPanel_"+prov+".csv"

##START
### create array to store info
### for assign value: res[row][col]=new value
### 53 week per year, 2011~2019: total 9; 9*52=468; +begin+end=470; +2015:53th week=471
rows, cols = (len(cat1_names)+len(cat2_names)+8+2, 1*471) 
res = [[0 for i in range(cols)] for j in range(rows)]

# position = 12 * (YYYY-2013) + (MM - 1)
# rows: month date
# col: province

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
            if row_i==0:
                # do nothing
                a=0
            else:
                city_str=splitRowInfo[3]
                current_cat1_str=splitRowInfo[8]
                current_cat2_str=splitRowInfo[9]

                post_title_str=splitRowInfo[6]
                post_content_str=splitRowInfo[11]
                reply_title_str=splitRowInfo[12]
                reply_content_str=splitRowInfo[13]
                post_str=post_content_str+post_title_str
                reply_str=reply_content_str+reply_title_str

                post_status=splitRowInfo[7]

                post_time_str=int(splitRowInfo[10][0:4]+splitRowInfo[10][5:7]+splitRowInfo[10][8:10])
                post_time_yyyy_str=int(splitRowInfo[10][0:4])
                post_time_mm_str=int(splitRowInfo[10][5:7])
                post_time_dd_str=int(splitRowInfo[10][8:10])
                if post_status=="待回复" or post_status=="办理中":
                    reply_time_str=-1
                    reply_time_yyyy_str=-1
                    reply_time_mm_str=-1
                    reply_time_dd_str=-1
                else:
                    if (splitRowInfo[14][0]=='2'):
                        reply_time_str=int(splitRowInfo[14][0:4]+splitRowInfo[14][5:7]+splitRowInfo[14][8:10])  
                        reply_time_yyyy_str=int(splitRowInfo[14][0:4])
                        reply_time_mm_str=int(splitRowInfo[14][5:7])
                        reply_time_dd_str=int(splitRowInfo[14][8:10])
                    elif (splitRowInfo[15][0]=='2'):
                        reply_time_str=int(splitRowInfo[15][0:4]+splitRowInfo[15][5:7]+splitRowInfo[15][8:10])
                        reply_time_yyyy_str=int(splitRowInfo[15][0:4])
                        reply_time_mm_str=int(splitRowInfo[15][5:7])
                        reply_time_dd_str=int(splitRowInfo[15][8:10])
                    elif (splitRowInfo[16][0]=='2'):
                        reply_time_str=int(splitRowInfo[16][0:4]+splitRowInfo[16][5:7]+splitRowInfo[16][8:10])
                        reply_time_yyyy_str=int(splitRowInfo[16][0:4])
                        reply_time_mm_str=int(splitRowInfo[16][5:7])
                        reply_time_dd_str=int(splitRowInfo[16][8:10])
                    elif (splitRowInfo[17][0]=='2'):
                        reply_time_str=int(splitRowInfo[17][0:4]+splitRowInfo[17][5:7]+splitRowInfo[17][8:10])
                        reply_time_yyyy_str=int(splitRowInfo[17][0:4])
                        reply_time_mm_str=int(splitRowInfo[17][5:7])
                        reply_time_dd_str=int(splitRowInfo[17][8:10])
                   

                #to decide which week for post time
                #(2011, 52, 6) or 201101
                post_time_week=-1
                post_time_week_yyyy=datetime.date(post_time_yyyy_str,post_time_mm_str,post_time_dd_str).isocalendar()[0]
                post_time_week_mm=datetime.date(post_time_yyyy_str,post_time_mm_str,post_time_dd_str).isocalendar()[1]
                if post_time_week_yyyy<2011 and post_time_str>=20110101:
                    post_time_week=0
                elif post_time_week_yyyy<=2015:
                    post_time_week=(post_time_week_yyyy-2011)*52+post_time_week_mm
                elif post_time_week_yyyy>2015 and post_time_week_yyyy<=2019:
                    post_time_week=(post_time_week_yyyy-2011)*52+1+post_time_week_mm
                elif post_time_week_yyyy>2019 and post_time_str<20200101:
                    post_time_week=470

                reply_time_week=-1
                if post_status!="待回复" and post_status!="办理中":
                    reply_time_week_yyyy=datetime.date(reply_time_yyyy_str,reply_time_mm_str,reply_time_dd_str).isocalendar()[0]
                    reply_time_week_mm=datetime.date(reply_time_yyyy_str,reply_time_mm_str,reply_time_dd_str).isocalendar()[1]
                    if reply_time_week_yyyy<2011 and reply_time_str>=20110101:
                        reply_time_week=0
                    elif reply_time_week_yyyy<=2015:
                        reply_time_week=(reply_time_week_yyyy-2011)*52+reply_time_week_mm
                    elif reply_time_week_yyyy>2015 and reply_time_week_yyyy<=2019:
                        reply_time_week=(reply_time_week_yyyy-2011)*52+1+reply_time_week_mm
                    elif reply_time_week_yyyy>2019 and reply_time_str<20200101:
                        reply_time_week=470

                # for post keyword cat 
                # for reply keyword cat 
                Row=0
                Col=0
                for city_i in range(1):
                    # if citiesInProv[city_i] == city_str:
                        # if in the same city
                        if post_time_week>=0:
                            # check post/reply contains any keyword?
                            for keyWord_cat_i in range (4):
                                if keyWord_cat_i==0: 
                                    keyWord_cat=keyWord_cat0
                                    keywords=keywords0
                                elif keyWord_cat_i==1: 
                                    keyWord_cat=keyWord_cat1
                                    keywords=keywords1
                                elif keyWord_cat_i==2: 
                                    keyWord_cat=keyWord_cat2
                                    keywords=keywords2
                                else: 
                                    keyWord_cat=keyWord_cat3
                                    keywords=keywords3

                                for keyword in keywords:
                                    b1=post_str.find(keyword)
                                    if (b1>=0):
                                        Row=keyWord_cat_i
                                        Col=city_i*471+post_time_week
                                        res[Row][Col]+=1
                                        break

                                    if reply_time_week>=0:
                                        b2=reply_str.find(keyword)
                                        if (b2>=0):
                                            if reply_time_week>=0:
                                                Row=keyWord_cat_i+4
                                                Col=city_i*471+reply_time_week
                                                res[Row][Col]+=1
                                                break

                            # check cat
                            for cat1_i in range(int(len(cat1_names))):
                                if cat1_names[cat1_i] == current_cat1_str:
                                    Row=cat1_i+8
                                    Col=city_i*471+post_time_week
                                    res[Row][Col]+=1
                                    break
                            for cat2_i in range(int(len(cat2_names))):
                                if cat2_names[cat2_i] == current_cat2_str:
                                    Row=cat2_i+len(cat1_names)+8
                                    Col=city_i*471+post_time_week
                                    res[Row][Col]+=1
                                    break

                            #check total num of post 
                            Row=len(cat2_names)+len(cat1_names)+8
                            Col=city_i*471+post_time_week
                            res[Row][Col]+=1
                            #check total num of reply
                            if reply_time_week>=0:
                                Row=len(cat2_names)+len(cat1_names)+9
                                Col=city_i*471+reply_time_week
                                res[Row][Col]+=1
            
        except:
            continue



###Print out result to file

## Print first row: city
outFile = open(output_name,"a",encoding="utf8")
output=",,"
for i in range (1):
    for j in range (471):
        output+=prov+","
output+="\n"
outFile.writelines(output)
outFile.close()
 
## Print 2nd row: week number
outFile = open(output_name,"a",encoding="utf8")
output=",,"
for i in range (1):
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
        output="KeywordType_Post, 工程建设"
    elif row_num==1:
        output="KeywordType_Post, 一号工程"
    elif row_num==2:
        output="KeywordType_Post, 环保"
    elif row_num==3:
        output="KeywordType_Post, 招商引资"

    elif row_num==4:
        output="KeywordType_Reply, 工程建设"
    elif row_num==5:
        output="KeywordType_Reply, 一号工程"
    elif row_num==6:
        output="KeywordType_Reply, 环保"
    elif row_num==7:
        output="KeywordType_Reply, 招商引资"

    elif 7<row_num and row_num<(len(cat1_names)+8):
        output="Cat for Post&Reply, Cat1"+cat1_names[row_num-8]
    elif row_num<(len(cat2_names)+len(cat1_names)+8):
        output="Cat for Post&Reply, Cat2"+cat2_names[row_num-8-len(cat1_names)]
    elif row_num==(len(cat2_names)+len(cat1_names)+8):
        output=", Total numer of Posts"
    elif row_num==(len(cat2_names)+len(cat1_names)+9):
        output=", Total numer of Replies"

    outFile = open(output_name,"a",encoding="utf8")
    output=output+","

    for i in range (1*471):
        output=output+str(res[row_num][i])+","
    output=output+"\n"
    # print(output)
    outFile.writelines(output)
    outFile.close()

    row_num+=1

print("done!")