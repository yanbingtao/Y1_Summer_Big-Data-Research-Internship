import csv
import operator

# prov="云南省"
# citiesInProv=["临沧市", "丽江市", "保山市", "大理州", "德宏州", "怒江州", "文山州", "昆明市", "昭通市", "普洱市", "曲靖市", "楚雄州", "玉溪市", "红河州", "西双版纳州", "迪庆州"]
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
# prov="山西省_updated"
# citiesInProv=["临汾市", "吕梁市", "大同市", "太原市", "忻州市", "晋中市", "晋城市", "朔州市", "运城市", "长治市", "阳泉市"]
# prov="广东省"
# citiesInProv=["东莞市", "云浮市", "佛山市", "广州市", "惠州市", "揭阳市", "梅州市", "汕头市", "汕尾市", "江门市", "河源市", "深圳市", "清远市", "湛江市", "潮州市", "珠海市", "肇庆市", "茂名市", "阳江市", "韶关市"]
# prov="广西省"
# citiesInProv=["北海市", "南宁市", "柳州市", "桂林市", "梧州市", "玉林市", "百色市", "贵港市", "贺州市", "钦州市", "防城港市"]
prov="新疆维吾尔自治区" #???省辖县(县级市)
citiesInProv=["乌鲁木齐市", "伊犁哈萨克自治州", "克孜勒苏柯尔克孜自治州", "克拉玛依市", "博尔塔拉蒙古自治州", "吐鲁番市", "和田地区", "哈密市", "喀什地区", "塔城地区", "巴音郭楞蒙古自治州", "昌吉回族自治州", "阿克苏地区", "阿勒泰地区"]
# prov="江苏省"
# citiesInProv=["南京市", "南通市", "宿迁市", "常州市", "徐州市", "扬州市", "无锡市", "泰州市", "淮安市", "盐城市", "苏州市", "连云港市", "镇江市"]
# prov="江西省"
# citiesInProv=["上饶市", "九江市", "南昌市", "吉安市", "宜春市", "抚州市", "新余市", "景德镇市", "萍乡市", "赣州市", "鹰潭市"]
# prov="河北省"
# citiesInProv=["唐山市", "石家庄市", "秦皇岛市"]
# prov="河北省_updated"
# citiesInProv=["保定市", "唐山市", "定州市", "廊坊市", "张家口市", "承德市", "沧州市", "石家庄市", "秦皇岛市", "衡水市", "辛集市", "邢台市", "邯郸市", "雄安新区"]
# prov="河南省"
# citiesInProv=["三门峡市", "信阳市", "兰考县", "南阳市", "周口市", "商丘市", "固始县", "安阳市", "巩义市", "开封市", "新乡市", "新蔡县", "永城市", "汝州市", "洛阳市", "济源市", "滑县", "漯河市", "濮阳市", "焦作市", "许昌市", "邓州市", "长垣市", "驻马店市", "鹤壁市", "鹿邑县"]
# prov="浙江省"
# citiesInProv=["丽水市", "台州市", "嘉兴市", "宁波市", "杭州市", "温州市", "湖州市", "绍兴市", "舟山市", "衢州市", "金华市"]
# prov="海南省"#???省辖县(县级市)
# citiesInProv=["三亚市", "三沙市", "儋州市", "海口市"]
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
path=r"C:\Users\yanbi\Desktop\Sum_Research2\National data"
filename= path+"\All_"+prov+".csv"


path_out=r"C:\Users\yanbi\Desktop\Sum_Research2\RawData\ReplyTimeByCity"
output_name= path_out + "\getPosttimeNReplytime_ByCity_"+prov+".csv"


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