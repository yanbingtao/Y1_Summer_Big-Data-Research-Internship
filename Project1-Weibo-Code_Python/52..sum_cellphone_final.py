# tweets_extract_1_include_time_with_cat_cat0 split to quarters

import csv
import glob

cat=4
file_path_in =r"C:\Users\yanbi\Desktop\Sum_Research\STAGE3-SPLIT_by_Quarters\CAT"+str(cat)+"\ori\cellphone_sum.csv"
# file_name_list = glob.glob(file_path_in+"/*cellphone.csv")

file_path_out =r"C:\Users\yanbi\Desktop\Sum_Research\STAGE3-SPLIT_by_Quarters\CAT"+str(cat)+"\ori\cellphone_sum_final.csv"
# file_name_list = glob.glob(file_path+"/*jieba.csv")

a_rows, a_cols = (100000, 100) 
res = [[0 for i in range(a_cols)] for j in range(a_rows)] 
index_b=1
index_q=1

t_tweets_ori = open(file_path_in,"r", encoding="utf8")
rows = 0
for row in t_tweets_ori:
    rows += 1

t_tweets_ori = open(file_path_in,"r", encoding="utf8")

# //input all brands
for i_split in range (rows):
    tweets_ori_info = t_tweets_ori.readline()
    split_tweets_ori_info=tweets_ori_info.split(",")
    # 
    l=len(split_tweets_ori_info)
    # 

    if len(split_tweets_ori_info)==1:
        date=split_tweets_ori_info[0][0:len(split_tweets_ori_info[0])-1]
        res[0][index_q]=date
        index_q=index_q+1

    # fill in num
    if len(split_tweets_ori_info)==2:
        flag = False
        current_brand=split_tweets_ori_info[0]
        current_num=split_tweets_ori_info[1][0:len(split_tweets_ori_info[1])-1]
        for i in range (index_b):
            if current_brand==res[i][0]:
                flag=True
                res[i][index_q-1]=current_num
                break
        if (flag==False):
            res[index_b][0]=current_brand
            res[index_b][index_q-1]=current_num
            index_b=index_b+1

# output
outFile = open(file_path_out,"w",encoding="utf8")
for i in range (index_b):
    outstr=""
    for j in range(index_q):
        outstr=outstr+str(res[i][j])+","
    outstr+="\n"
    outFile.writelines(outstr)

outFile.close()