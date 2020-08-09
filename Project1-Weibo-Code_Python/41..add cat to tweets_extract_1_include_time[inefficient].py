# add cat to "tweets_extract_1_include_time"

import csv
# t_user = open(r"C:\Users\yanbi\Desktop\Sum_Research\user107.csv","r",encoding="utf8")
t_tweets_ori = open(r"C:\Users\yanbi\Desktop\Sum_Research\tweets_extract_1_include_time.csv","r",encoding="utf8")
cat=open(r"C:\Users\yanbi\Desktop\Sum_Research\users1000fs_sum_cat_all.csv","r",encoding="utf8")

outFile = open(r"C:\Users\yanbi\Desktop\Sum_Research\tweets_extract_1_include_time_with_cat.csv","w",encoding="utf8")


# num_rows_1000 = 0
# for row in cat:
#     num_rows_1000 += 1

# num_rows_1500 = 0
# for row in t_tweets:
#     num_rows_1500 += 1

# num_rows_1000=6
tweets_ori_rows=3417127
cat_rows=1499
# t=9831
# t2=14960

for i in range(tweets_ori_rows):
    tweets_ori_info = t_tweets_ori.readline()
    split_tweets_ori_info=tweets_ori_info.split(",")
    try:
        str1_UserID=int(split_tweets_ori_info[0])
        cat=open(r"C:\Users\yanbi\Desktop\Sum_Research\users1000fs_sum_cat_all.csv","r",encoding="utf8")
        for j in range (cat_rows):
            cat_r=cat.readline()
            split_cat_r=cat_r.split(",")
            try:
                str2_UserID=int(split_cat_r[1])
                if (str1_UserID==str2_UserID):
                    out_str=split_cat_r[0]+","+tweets_ori_info
                    outFile.writelines(out_str)
                    break
            except:
                continue
       
    except:
        continue




t_tweets_ori.close()
cat.close()
outFile.close()