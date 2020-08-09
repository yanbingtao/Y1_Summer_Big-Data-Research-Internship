# extract tweets from "tweets_extract_1_include_time.csv", and output file based on cat

import csv
# t_user = open(r"C:\Users\yanbi\Desktop\Sum_Research\user107.csv","r",encoding="utf8")
# t_tweets = open(r"C:\Users\yanbi\Desktop\Sum_Research\tweets_extract_1_include_time.csv","r",encoding="utf8")
ref=open(r"C:\Users\yanbi\Desktop\Sum_Research\users1000fs_sum_cat_all.csv")
# ref=open(r"C:\Users\yanbi\Desktop\Sum_Research\users1000fs_sum_cat_107.csv")
outFile = open(r"C:\Users\yanbi\Desktop\Sum_Research\cat4_tweets.csv","w",encoding="utf8")
cat=4

# t_tweets = open(r"C:\Users\yanbi\Desktop\Sum_Research\user111_tweets.csv","r",encoding="utf8")
# ref_row = 0
# for row in t_tweets:
#     ref_row += 1

ref_row=1499
t_tweets_row=3417127
tweets_107_row=21888
tweets_108_row=914732
tweets_109_row=1003746
tweets_110_row=881153
tweets_111_row=595606

# t_user = open(r"C:\Users\yanbi\Desktop\Sum_Research\user107.csv","r",encoding="utf8")
# t_tweets = open(r"C:\Users\yanbi\Desktop\Sum_Research\tweets_extract_1_include_time.csv","r",encoding="utf8")
ref=open(r"C:\Users\yanbi\Desktop\Sum_Research\users1000fs_sum_cat_all.csv")
# ref=open(r"C:\Users\yanbi\Desktop\Sum_Research\users1000fs_sum_cat_107.csv")

for i in range(ref_row):
    # file_1000_user=t_user.renum_rows_1500dline()
    if (i==49):
        a=0
    ref_line = ref.readline()
    split_ref_line=ref_line.split(",")
    try:
        str1=int(split_ref_line[0])
        str2_userID=int(split_ref_line[1])
        if (str1==cat):
            # go to t_tweets to find all related entries
            if (str2_userID>1070000000 and str2_userID<=1080000000):
                t_tweets = open(r"C:\Users\yanbi\Desktop\Sum_Research\user107_tweets.csv","r",encoding="utf8")
                for i_107 in range(tweets_107_row):
                    tweets_107_line = t_tweets.readline()
                    split_tweets_107_line=tweets_107_line.split(",")
                    t107_str1=int(split_tweets_107_line[0])
                    if (t107_str1 == str2_userID):
                        outFile.writelines(tweets_107_line)
                    
            if (str2_userID>1080000000 and str2_userID<=1090000000):
                t_tweets = open(r"C:\Users\yanbi\Desktop\Sum_Research\user108_tweets.csv","r",encoding="utf8")
                for i_108 in range(tweets_108_row):
                    tweets_108_line = t_tweets.readline()
                    split_tweets_108_line=tweets_108_line.split(",")
                    t108_str1=int(split_tweets_108_line[0])
                    if (t108_str1 == str2_userID):
                        outFile.writelines(tweets_108_line)

            if (str2_userID>1090000000 and str2_userID<=1100000000):
                t_tweets = open(r"C:\Users\yanbi\Desktop\Sum_Research\user109_tweets.csv","r",encoding="utf8")
                for i_109 in range(tweets_109_row):
                    tweets_109_line = t_tweets.readline()
                    split_tweets_109_line=tweets_109_line.split(",")
                    t109_str1=int(split_tweets_109_line[0])
                    if (t109_str1 == str2_userID):
                        outFile.writelines(tweets_109_line)

            if (str2_userID>1100000000 and str2_userID<=1110000000):
                t_tweets = open(r"C:\Users\yanbi\Desktop\Sum_Research\user110_tweets.csv","r",encoding="utf8")
                for i_110 in range(tweets_110_row):
                    tweets_110_line = t_tweets.readline()
                    split_tweets_110_line=tweets_110_line.split(",")
                    t110_str1=int(split_tweets_110_line[0])
                    if (t110_str1 == str2_userID):
                        outFile.writelines(tweets_110_line)

            if (str2_userID>1110000000 and str2_userID<=1120000000):
                t_tweets = open(r"C:\Users\yanbi\Desktop\Sum_Research\user111_tweets.csv","r",encoding="utf8")
                for i_111 in range(tweets_111_row):
                    tweets_111_line = t_tweets.readline()
                    split_tweets_111_line=tweets_111_line.split(",")
                    t111_str1=int(split_tweets_111_line[0])
                    if (t111_str1 == str2_userID):
                        outFile.writelines(tweets_111_line)

    except:
        continue




t_tweets.close()
outFile.close()