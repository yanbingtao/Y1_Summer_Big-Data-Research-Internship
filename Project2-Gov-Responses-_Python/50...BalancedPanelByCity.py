import csv
import operator
import math as math
import datetime

# provs=["云南省","内蒙古","吉林省","四川省","宁夏回族自治区","安徽省","山东省","山西省","广东省","广西省","江苏省","江西省","河北省","河南省","浙江省","湖北省","湖南省","甘肃省","福建省","西藏自治区","贵州省","辽宁省","陕西省","青海省","黑龙江省"]

prov="云南省"
citiesInProv=["临沧市", "丽江市", "保山市", "大理州", "德宏州", "怒江州", "文山州", "昆明市", "昭通市", "普洱市", "曲靖市", "楚雄州", "玉溪市", "红河州", "西双版纳州", "迪庆州"]
# prov="内蒙古"
# citiesInProv=["乌兰察布市", "乌海市", "兴安盟", "包头市", "呼伦贝尔市", "呼和浩特市", "巴彦淖尔市", "赤峰市", "通辽市", "鄂尔多斯市", "锡林郭勒盟", "阿拉善盟"]
# prov="吉林省"
# citiesInProv=["吉林市", "四平市", "延边朝鲜族自治州", "松原市", "白城市", "白山市", "辽源市", "通化市", "长春市"]
# prov="四川省"
# citiesInProv=["乐山市", "内江市", "凉山州", "南充市", "宜宾市", "巴中市", "广元市", "广安市", "德阳市", "成都市", "攀枝花市", "泸州市", "甘孜州", "眉山市", "绵阳市", "自贡市", "资阳市", "达州市", "遂宁市", "阿坝州", "雅安市"]
# prov="宁夏回族自治区"
# citiesInProv=["中卫市", "吴忠市", "固原市", "石嘴山市", "银川市"]
# prov="安徽省"
# citiesInProv=["亳州市", "六安市", "合肥市", "安庆市", "宣城市", "宿州市", "池州市", "淮北市", "淮南市", "滁州市", "芜湖市", "蚌埠市", "铜陵市", "阜阳市", "马鞍山市", "黄山市"]
# prov="山东省"
# citiesInProv=["东营市", "临沂市", "威海市", "德州市", "日照市", "枣庄市", "泰安市", "济南市", "济宁市", "淄博市", "滨州市", "潍坊市", "烟台市", "聊城市", "菏泽市", "青岛市"]
# prov="山西省"
# citiesInProv=["临汾市", "吕梁市", "大同市", "太原市", "忻州市", "晋中市", "晋城市", "朔州市", "运城市", "长治市", "阳泉市"]
# prov="广东省"
# citiesInProv=["东莞市", "云浮市", "佛山市", "广州市", "惠州市", "揭阳市", "梅州市", "汕头市", "汕尾市", "江门市", "河源市", "深圳市", "清远市", "湛江市", "潮州市", "珠海市", "肇庆市", "茂名市", "阳江市", "韶关市"]
# prov="广西省"
# citiesInProv=["北海市", "南宁市", "柳州市", "桂林市", "梧州市", "玉林市", "百色市", "贵港市", "贺州市", "钦州市", "防城港市"]
# prov="江苏省"
# citiesInProv=["南京市", "南通市", "宿迁市", "常州市", "徐州市", "扬州市", "无锡市", "泰州市", "淮安市", "盐城市", "苏州市", "连云港市", "镇江市"]
# prov="江西省"
# citiesInProv=["上饶市", "九江市", "南昌市", "吉安市", "宜春市", "抚州市", "新余市", "景德镇市", "萍乡市", "赣州市", "鹰潭市"]
# prov="河北省"
# citiesInProv=["保定市", "唐山市", "定州市", "廊坊市", "张家口市", "承德市", "沧州市", "石家庄市", "秦皇岛市", "衡水市", "辛集市", "邢台市", "邯郸市", "雄安新区"]
# prov="河南省"
# citiesInProv=["三门峡市", "信阳市", "兰考县", "南阳市", "周口市", "商丘市", "固始县", "安阳市", "巩义市", "开封市", "新乡市", "新蔡县", "永城市", "汝州市", "洛阳市", "济源市", "滑县", "漯河市", "濮阳市", "焦作市", "许昌市", "邓州市", "长垣市", "驻马店市", "鹤壁市", "鹿邑县"]
# prov="浙江省"
# citiesInProv=["丽水市", "台州市", "嘉兴市", "宁波市", "杭州市", "温州市", "湖州市", "绍兴市", "舟山市", "衢州市", "金华市"]
# prov="湖北省"
# citiesInProv=["仙桃市", "十堰市", "咸宁市", "天门市", "孝感市", "宜昌市", "恩施州", "武汉市", "潜江市", "神农架林区", "荆州市", "荆门市", "襄阳市", "鄂州市", "随州市", "黄冈市", "黄石市"]
# prov="湖南省"
# citiesInProv=["娄底市", "岳阳市", "常德市", "张家界市", "怀化市", "株洲市", "永州市", "湘潭市", "湘西州", "益阳市", "衡阳市", "邵阳市", "郴州市", "长沙市"]
# prov="甘肃省"
# citiesInProv=["临夏州", "兰州市", "嘉峪关市", "天水市", "定西市", "平凉市", "庆阳市", "张掖市", "武威市", "甘南州", "白银市", "酒泉市", "金昌市", "陇南市"]
# prov="福建省"
# citiesInProv=["三明市", "南平市", "厦门市", "宁德市", "平潭综合实验区", "泉州市", "漳州市", "莆田市", "龙岩市"]
# prov="西藏自治区"
# citiesInProv=["山南市", "拉萨市", "日喀则市", "昌都市", "林芝市", "那曲市", "阿里地区"]
# prov="贵州省"
# citiesInProv=["六盘水市", "安顺市", "毕节市", "贵安新区", "贵阳市", "遵义市", "铜仁市", "黔东南州", "黔南州", "黔西南州"]
# prov="辽宁省"
# citiesInProv=["丹东市", "大连市", "抚顺市", "朝阳市", "本溪市", "沈阳市", "盘锦市", "营口市", "葫芦岛市", "辽阳市", "铁岭市", "锦州市", "阜新市", "鞍山市"]
# prov="陕西省"
# citiesInProv=["咸阳市", "商洛市", "安康市", "宝鸡市", "延安市", "榆林市", "杨凌示范区", "汉中市", "渭南市", "西安市", "铜川市"]
# prov="青海省"
# citiesInProv=["果洛藏族自治州", "海东市", "海北藏族自治州", "海南藏族自治州", "海西蒙古族藏族自治州", "玉树藏族自治州", "西宁市", "黄南藏族自治州"]
# prov="黑龙江省"
# citiesInProv=["七台河市", "伊春市", "佳木斯市", "双鸭山市", "哈尔滨市", "大兴安岭地区", "大庆市", "牡丹江市", "绥化市", "鸡西市", "鹤岗市", "黑河市", "齐齐哈尔市"]

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
rows, cols = (len(cat1_names)+len(cat2_names)+8+2, len(citiesInProv)*471) 
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
                if post_time_week_yyyy==2010 and post_time_str>=20110101:
                    post_time_week=0
                elif post_time_week_yyyy<=2015:
                    post_time_week=(post_time_week_yyyy-2011)*52+post_time_week_mm
                elif post_time_week_yyyy>2015 and post_time_week_yyyy<=2019:
                    post_time_week=(post_time_week_yyyy-2011)*52+1+post_time_week_mm
                elif post_time_week_yyyy==2020 and post_time_str<20200101:
                    post_time_week=470

                reply_time_week=-1
                if post_status!="待回复" and post_status!="办理中":
                    reply_time_week_yyyy=datetime.date(reply_time_yyyy_str,reply_time_mm_str,reply_time_dd_str).isocalendar()[0]
                    reply_time_week_mm=datetime.date(reply_time_yyyy_str,reply_time_mm_str,reply_time_dd_str).isocalendar()[1]
                    if reply_time_week_yyyy==2010 and reply_time_str>=20110101:
                        reply_time_week=0
                    elif reply_time_week_yyyy<=2015:
                        reply_time_week=(reply_time_week_yyyy-2011)*52+reply_time_week_mm
                    elif reply_time_week_yyyy>2015 and reply_time_week_yyyy<=2019:
                        reply_time_week=(reply_time_week_yyyy-2011)*52+1+reply_time_week_mm
                    elif reply_time_week_yyyy==2020 and reply_time_str<20200101:
                        reply_time_week=470
            

                # for post keyword cat 
                # for reply keyword cat 
                Row=0
                Col=0
                for city_i in range(int(len(citiesInProv))):
                    if citiesInProv[city_i] == city_str:
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
for i in range (len(citiesInProv)):
    for j in range (471):
        output+=citiesInProv[i]+","
output+="\n"
outFile.writelines(output)
outFile.close()
 
## Print 2nd row: week number
outFile = open(output_name,"a",encoding="utf8")
output=",,"
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

    for i in range (len(citiesInProv)*471):
        output=output+str(res[row_num][i])+","
    output=output+"\n"
    # print(output)
    outFile.writelines(output)
    outFile.close()

    row_num+=1

print("done!")