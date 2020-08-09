# tweets_extract_1_include_time_with_cat_cat0 split to quarters

import csv
cat=4
t_tweets_ori = open(r"C:\Users\yanbi\Desktop\Sum_Research\tweets_extract_1_include_time_with_cat_cat"+str(cat)+".csv","r",encoding="utf8")
# outFile = open(r"C:\Users\yanbi\Desktop\Sum_Research\tweets_extract_1_include_time_with_cat_cat0_quarters.csv","a",encoding="utf8")

num_rows_1500 = 0
for row in t_tweets_ori:
    num_rows_1500 += 1

tweets_ori_rows=num_rows_1500

t_tweets_ori = open(r"C:\Users\yanbi\Desktop\Sum_Research\tweets_extract_1_include_time_with_cat_cat"+str(cat)+".csv","r",encoding="utf8")

for i in range(tweets_ori_rows):
    tweets_ori_info = t_tweets_ori.readline()
    split_tweets_ori_info=tweets_ori_info.split(",")
    try:
        date=split_tweets_ori_info[5]
        if len(date)==5:
            yy=2020
            mm=int(date[0:2])
            dd=int(date[3:5])
        if len(date)==10:
            yy=int(date[0:4])
            mm=int(date[5:7])
            dd=int(date[8:10])

        # output_file_name=""
        if (1<=mm and mm<=3):
            outFile = open(r"C:\Users\yanbi\Desktop\Sum_Research\STAGE3-SPLIT_by_Quarters\tweets_extract_1_include_time_with_cat_cat"+str(cat)+"_quarter_"+str(yy)+"_1st.csv","a",encoding="utf8")
            outFile.writelines(tweets_ori_info)
        elif (4<=mm and mm<=6):
            outFile = open(r"C:\Users\yanbi\Desktop\Sum_Research\STAGE3-SPLIT_by_Quarters\tweets_extract_1_include_time_with_cat_cat"+str(cat)+"_quarter_"+str(yy)+"_2nd.csv","a",encoding="utf8")
            outFile.writelines(tweets_ori_info)
        elif (7<=mm and mm<=9):
            outFile = open(r"C:\Users\yanbi\Desktop\Sum_Research\STAGE3-SPLIT_by_Quarters\tweets_extract_1_include_time_with_cat_cat"+str(cat)+"_quarter_"+str(yy)+"_3rd.csv","a",encoding="utf8")
            outFile.writelines(tweets_ori_info)
        elif (9<=mm and mm<=12):
            outFile = open(r"C:\Users\yanbi\Desktop\Sum_Research\STAGE3-SPLIT_by_Quarters\tweets_extract_1_include_time_with_cat_cat"+str(cat)+"_quarter_"+str(yy)+"_4th.csv","a",encoding="utf8")
            outFile.writelines(tweets_ori_info)
            
    except:
        continue




t_tweets_ori.close()
# cat.close()
outFile.close()