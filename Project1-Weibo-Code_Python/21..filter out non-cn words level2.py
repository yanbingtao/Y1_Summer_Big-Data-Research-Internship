# extract tweets only for 107 group users, sorted

import csv
# t_user = open(r"C:\Users\yanbi\Desktop\Sum_Research\user108.csv","r",encoding="utf8")
t_tweets = open(r"C:\Users\yanbi\Desktop\Sum_Research\cat4_tweets_text.csv","r",encoding="utf8")
outFile = open(r"C:\Users\yanbi\Desktop\Sum_Research\cat4_tweets_text2.csv","w",encoding="utf8")


file_1500_tweets = t_tweets.readline()
split_1500_tweets=file_1500_tweets.split(",")

for i in range (len(split_1500_tweets)):
    out_str=split_1500_tweets[i]
    try:
        words_out = ["！","《","》","…","?",".","年",";","月","日","的",":",";","还","和","太","非常","最","更","也","都","@","再","也","为","#","-","。","，","[","]","_"]
        for j in range (len(words_out)):
            out_str=out_str.replace(words_out[j],"")
        outFile.writelines(out_str)
    except:
        continue

t_tweets.close()
outFile.close()