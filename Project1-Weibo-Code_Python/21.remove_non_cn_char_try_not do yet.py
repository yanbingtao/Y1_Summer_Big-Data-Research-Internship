# extract tweets only for 107 group users, sorted

import csv
# t_user = open(r"C:\Users\yanbi\Desktop\Sum_Research\user108.csv","r",encoding="utf8")
t_tweets = open(r"C:\Users\yanbi\Desktop\Sum_Research\user107_tweets_unsorted.csv","r",encoding="utf8")
outFile = open(r"C:\Users\yanbi\Desktop\Sum_Research\test2.csv","w",encoding="utf8")


# num_rows_1000 = 0
# for row in t_user:
#     num_rows_1000 += 1

num_rows_1500 = 0
for row in t_tweets:
    num_rows_1500 += 1

# num_rows_1000=6
# num_rows_1500=3417597
# t=9831
# t2=14960

# t_user = open(r"C:\Users\yanbi\Desktop\Sum_Research\user107.csv","r",encoding="utf8")
t_tweets = open(r"C:\Users\yanbi\Desktop\Sum_Research\user107_tweets_unsorted.csv","r",encoding="utf8")

# for i in range (num_rows_1000):
#     file_1000_user=t_user.readline()
#     t_tweets = open(r"C:\Users\yanbi\Desktop\Sum_Research\user108_tweets_unsorted.csv","r",encoding="utf8")
    
for j in range (num_rows_1500):
    file_1500_tweets = t_tweets.readline()
    split_1500_tweets=file_1500_tweets.split(",")
    try:
        str2=int(split_1500_tweets[0])
        if (str2>=1060000000 and str2<=1080000000):
            out_str=""
            out_str = split_1500_tweets[2]+","
            outFile.writelines(out_str)
    except:
        continue

# for i in range(num_rows_1500):
#     # file_1000_user=t_user.renum_rows_1500dline()
#     file_1500_tweets = t_tweets.readline()
#     split_1500_tweets=file_1500_tweets.split(",")
#     # t_tweets = open(r"C:\Users\yanbi\Desktop\Sum_Research\tweets_extract_0.csv","r",encoding="utf8")
#     t_user = open(r"C:\Users\yanbi\Desktop\Sum_Research\user107.csv","r",encoding="utf8")
#     for j in range (num_rows_1000):
#         # file_1500_tweets = t_tweets.readline()
#         # split_1500_tweets=file_1500_tweets.split(",")
#         file_1000_user=t_user.readline()
#         try:
#             str1=int(file_1000_user)
#             str2=int(split_1500_tweets[0])
#             if (str1==str2):
#                 out_str=""
#                 out_str = split_1500_tweets[0]+","+split_1500_tweets[1]+","+split_1500_tweets[2]+","+split_1500_tweets[3]
#                 outFile.writelines(out_str)
#                 break
#         except:
#             continue




# t_user.close()
t_tweets.close()
outFile.close()