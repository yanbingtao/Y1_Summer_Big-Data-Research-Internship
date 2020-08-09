# extract tweets only for 107 group users, sorted

import csv
# t_user = open(r"C:\Users\yanbi\Desktop\Sum_Research\user108.csv","r",encoding="utf8")
t_tweets = open(r"C:\Users\yanbi\Desktop\Sum_Research\cat4_tweets.csv","r",encoding="utf8")
outFile = open(r"C:\Users\yanbi\Desktop\Sum_Research\cat4_tweets_text.csv","w",encoding="utf8")

num_rows_1500 = 0
for row in t_tweets:
    num_rows_1500 += 1

# t_user = open(r"C:\Users\yanbi\Desktop\Sum_Research\user107.csv","r",encoding="utf8")
t_tweets = open(r"C:\Users\yanbi\Desktop\Sum_Research\cat4_tweets.csv","r",encoding="utf8")

# for i in range (num_rows_1000):
#     file_1000_user=t_user.readline()
#     t_tweets = open(r"C:\Users\yanbi\Desktop\Sum_Research\user108_tweets_unsorted.csv","r",encoding="utf8")
    
for j in range (num_rows_1500):
    file_1500_tweets = t_tweets.readline()
    split_1500_tweets=file_1500_tweets.split(",")
    try:
        out_str=""
        out_str = split_1500_tweets[2]+","
        # filter out non cn word 
        for jj in range (len(out_str)):
            char = out_str[jj]
            if (char=="/" or char=='<' or char=='>' or (char>="0" and char<="9") or (char>="a" and char<="z") or char=='=' or char=='&' or char=='%' or (char>="A" and char<="Z")):
                out_str=out_str.replace(char," ")


        out_str=out_str.replace(" ","")
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