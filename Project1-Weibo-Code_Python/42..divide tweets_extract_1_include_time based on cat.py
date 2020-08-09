# add cat to "tweets_extract_1_include_time"

import csv
# t_user = open(r"C:\Users\yanbi\Desktop\Sum_Research\user107.csv","r",encoding="utf8")
t_tweets_ori = open(r"C:\Users\yanbi\Desktop\Sum_Research\tweets_extract_1_include_time_with_cat.csv","r",encoding="utf8")
# cat=open(r"C:\Users\yanbi\Desktop\Sum_Research\users1000fs_sum_cat_all.csv","r",encoding="utf8")

outFile = open(r"C:\Users\yanbi\Desktop\Sum_Research\tweets_extract_1_include_time_with_cat_cat4.csv","w",encoding="utf8")
cat=4

# num_rows_1000 = 0
# for row in cat:
#     num_rows_1000 += 1

# num_rows_1500 = 0
# for row in t_tweets:
#     num_rows_1500 += 1

# num_rows_1000=6
tweets_ori_rows=3417127
# t=9831
# t2=14960

for i in range(tweets_ori_rows):
    tweets_ori_info = t_tweets_ori.readline()
    split_tweets_ori_info=tweets_ori_info.split(",")
    try:
        str1_cat=int(split_tweets_ori_info[0])
        if (str1_cat==cat):
            outFile.writelines(tweets_ori_info)
    except:
        continue




t_tweets_ori.close()
# cat.close()
outFile.close()