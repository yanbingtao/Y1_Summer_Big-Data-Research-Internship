# tweets_extract_1_include_time_with_cat_cat0 split to quarters

import csv
import glob

cat=4
file_path_in =r"C:\Users\yanbi\Desktop\Sum_Research\STAGE3-SPLIT_by_Quarters\CAT"+str(cat)+"\ori"
file_name_list = glob.glob(file_path_in+"/*cellphone.csv")

file_path_out =r"C:\Users\yanbi\Desktop\Sum_Research\STAGE3-SPLIT_by_Quarters\CAT"+str(cat)+"\ori\cellphone_sum.csv"
# file_name_list = glob.glob(file_path+"/*jieba.csv")


# need to read all files, for loop!!!
# 

for file_name_list_i in range (len(file_name_list)):
    t_tweets_ori = open(file_name_list[file_name_list_i],"r", encoding="utf8")
    tweets_ori_info = t_tweets_ori.readline()
    split_tweets_ori_info=tweets_ori_info.split(",")

    a_rows, a_cols = (100000, 2) 
    res = [[0 for i in range(a_cols)] for j in range(a_rows)] 
    index=0
    for i in range (len(split_tweets_ori_info)):
        current=split_tweets_ori_info[i]
        if index==0:
            res[index][0]=current
            index=index+1
        else:
            flag=False
            for j in range (index):
                if current==res[j][0]:
                    res[j][1]=res[j][1]+1
                    flag=True

            if (flag==False):
                res[index][0]=current
                index=index+1

    # output
    outFile = open(file_path_out,"a",encoding="utf8")
    # outFile.writelines("\n")
    outFile.writelines(file_name_list[file_name_list_i][122:131]+"Quarter"+"\n")
    # outFile.writelines("CAT"+str(cat)+"\n")
    for out_i in range (a_rows):
        current_brand=res[out_i][0]
        current_num=res[out_i][1]+1
        if (current_brand!=0 and current_brand!='' and current_num>1):
            outstr=current_brand+","+str(current_num)+"\n"
            outFile.writelines(outstr)



# for file_name_list_i in range (len(file_name_list)):
#     t_tweets_ori = open(file_name_list[file_name_list_i],"r", encoding="utf8")
#     tweets_ori_info = t_tweets_ori.read()
#     mytext = ",".join(jieba.cut(tweets_ori_info))
#     output_name=file_name_list[file_name_list_i][0:len(file_name_list[0])-4]+"_jieba.csv"
    
#     outFile = open(output_name,"a",encoding="utf8")
#     outFile.writelines(mytext)
#     outFile.close()