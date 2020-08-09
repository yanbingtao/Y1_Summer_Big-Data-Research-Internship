# tweets_extract_1_include_time_with_cat_cat0 split to quarters

import csv
import glob

cat=4
path =r"C:\Users\yanbi\Desktop\Sum_Research\STAGE3-SPLIT_by_Quarters\CAT"+str(cat)+"\ori"
file_name_list = glob.glob(path+"/*.csv")

for file_name_list_i in range (len(file_name_list)):
    t_tweets_ori = open(file_name_list[file_name_list_i],"r", encoding="utf8")

    num_rows_1500 = 0
    for row in t_tweets_ori:
        num_rows_1500 += 1

    tweets_ori_rows=num_rows_1500

    t_tweets_ori = open(file_name_list[file_name_list_i],"r", encoding="utf8")

    for i in range(tweets_ori_rows):
        tweets_ori_info = t_tweets_ori.readline()
        split_tweets_ori_info=tweets_ori_info.split(",")
        try:
            out_str=""
            out_str = split_tweets_ori_info[4]+","

            output_name=file_name_list[file_name_list_i][0:len(file_name_list[0])-4]+"_cellphone.csv"
            outFile = open(output_name,"a",encoding="utf8")
            outFile.writelines(out_str)
            outFile.close()
                
        except:
            continue




t_tweets_ori.close()
# cat.close()
