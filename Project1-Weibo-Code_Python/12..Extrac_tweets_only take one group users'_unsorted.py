# extract tweets only for 107 group users, sorted

import csv
# t_user = open(r"C:\Users\yanbi\Desktop\Sum_Research\user107.csv","r",encoding="utf8")
t_tweets = open(r"C:\Users\yanbi\Desktop\Sum_Research\tweets_extract_1_include_time.csv","r",encoding="utf8")
outFile = open(r"C:\Users\yanbi\Desktop\Sum_Research\user111_tweets.csv","w",encoding="utf8")


# num_rows_1000 = 0
# for row in t_user:
#     num_rows_1000 += 1

# num_rows_1500 = 0
# for row in t_tweets:
#     num_rows_1500 += 1

# num_rows_1000=6
num_rows_1500=3417127
# t=9831
# t2=14960

# t_user = open(r"C:\Users\yanbi\Desktop\Sum_Research\user107.csv","r",encoding="utf8")
t_tweets = open(r"C:\Users\yanbi\Desktop\Sum_Research\tweets_extract_1_include_time.csv","r",encoding="utf8")

for i in range(num_rows_1500):
    # file_1000_user=t_user.renum_rows_1500dline()
    file_1500_tweets = t_tweets.readline()
    split_1500_tweets=file_1500_tweets.split(",")
    # t_tweets = open(r"C:\Users\yanbi\Desktop\Sum_Research\tweets_extract_0.csv","r",encoding="utf8")
    # t_user = open(r"C:\Users\yanbi\Desktop\Sum_Research\user107.csv","r",encoding="utf8")
    # for j in range (num_rows_1000):
    #     # file_1500_tweets = t_tweets.readline()
    #     # split_1500_tweets=file_1500_tweets.split(",")
    #     file_1000_user=t_user.readline()
    try:
        str2=int(split_1500_tweets[0])
        if (str2>=1110000000 and str2<1120000000):
            out_str=""
            out_str = split_1500_tweets[0]+","+split_1500_tweets[1]+","+split_1500_tweets[2]+","+split_1500_tweets[3]+","+split_1500_tweets[4]+","+split_1500_tweets[5]
            outFile.writelines(out_str)
    except:
        continue




t_tweets.close()
outFile.close()