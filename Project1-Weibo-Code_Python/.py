# tweets_extract_1_include_time_with_cat_cat0 split to quarters

import csv
import glob
cat=4
path =r"C:\Users\yanbi\Desktop\Sum_Research\STAGE3-SPLIT_by_Quarters\CAT"+str(cat)
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
            out_str = split_tweets_ori_info[2]+","+split_tweets_ori_info[3]+","
            # filter out non cn word 
            for jj in range (len(out_str)):
                char = out_str[jj]
                if (char=="/" or char=='<' or char=='>' or (char>="0" and char<="9") or (char>="a" and char<="z") or char=='=' or char=='&' or char=='%' or (char>="A" and char<="Z")
                or char=="！"or char=="《" or char=="》" or char=="…" or char=="?" or char=="." or char=="年" or char==";" or char=="月" or char=="日" or char=="的" or char==":" or char==";"
                or char=="还" or char=="和" or char=="太" or char=="非常" or char=="最" or char=="更" or char=="也" or char=="都" or char=="@" or char=="再"or char=="也" or char=="为" or char=="#"
                or char=="-" or char=="。" or char=="，"or char=="[" or char=="]" or char=="_"):
                    out_str=out_str.replace(char," ")


            out_str=out_str.replace(" ","")

            output_name=file_name_list[file_name_list_i][0:len(file_name_list[0])-4]+"_tweets_text.csv"
            outFile = open(output_name,"a",encoding="utf8")
            outFile.writelines(out_str)
            outFile.close()
            # output_file_name=""
            # if (1<=mm and mm<=3):
            #     outFile = open(r"C:\Users\yanbi\Desktop\Sum_Research\STAGE3-SPLIT_by_Quarters\tweets_extract_1_include_time_with_cat_cat"+str(cat)+"_quarter_"+str(yy)+"_1st.csv","a",encoding="utf8")
            #     outFile.writelines(tweets_ori_info)
            # elif (4<=mm and mm<=6):
            #     outFile = open(r"C:\Users\yanbi\Desktop\Sum_Research\STAGE3-SPLIT_by_Quarters\tweets_extract_1_include_time_with_cat_cat"+str(cat)+"_quarter_"+str(yy)+"_2nd.csv","a",encoding="utf8")
            #     outFile.writelines(tweets_ori_info)
            # elif (7<=mm and mm<=9):
            #     outFile = open(r"C:\Users\yanbi\Desktop\Sum_Research\STAGE3-SPLIT_by_Quarters\tweets_extract_1_include_time_with_cat_cat"+str(cat)+"_quarter_"+str(yy)+"_3rd.csv","a",encoding="utf8")
            #     outFile.writelines(tweets_ori_info)
            # elif (9<=mm and mm<=12):
            #     outFile = open(r"C:\Users\yanbi\Desktop\Sum_Research\STAGE3-SPLIT_by_Quarters\tweets_extract_1_include_time_with_cat_cat"+str(cat)+"_quarter_"+str(yy)+"_4th.csv","a",encoding="utf8")
            #     outFile.writelines(tweets_ori_info)
                
        except:
            continue




t_tweets_ori.close()
# cat.close()
