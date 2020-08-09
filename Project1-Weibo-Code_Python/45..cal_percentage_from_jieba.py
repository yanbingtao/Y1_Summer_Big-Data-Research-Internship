# tweets_extract_1_include_time_with_cat_cat0 split to quarters

import csv
import glob

cat=4

path =r"C:\Users\yanbi\Desktop\Sum_Research\STAGE3-SPLIT_by_Quarters\CAT"+str(cat)
file_name_list = glob.glob(path+"/*jieba.csv")

num_of_word=0
total_words=0

for file_name_list_i in range (len(file_name_list)):
    t_tweets_ori = open(file_name_list[file_name_list_i],"r", encoding="utf8")

    num_rows_1500 = 0
    for row in t_tweets_ori:
        num_rows_1500 += 1

    tweets_ori_rows=num_rows_1500

    t_tweets_ori = open(file_name_list[file_name_list_i],"r", encoding="utf8")

    if (cat==0):
        words_set1=["中国","法治","改革","打四黑","除四害"]
        words_set2=["世界杯","皇马","球迷","巨星","观众"]
    if (cat==1):
        words_set1=["中国","法制报","神州","人民网","人民"]
        words_set2=["徐坤","电影","视频","明星榜","导演"]
    if (cat==2):
        words_set1=["新闻","中国","央视","政府","改革"]
        words_set2=["头条","粉丝","网红","快手","主持人"]
    if (cat==3):
        words_set1=["中国","中华","人民","央视","政府"]
        words_set2=["咖秀","中超","粉丝","球迷","世界杯"]
    if (cat==4):
        words_set1=["中华","公民","维稳","民主","祖国"]
        words_set2=["专辑","杨幂","春晚","主持人","男神"]

    outFile = open(r"C:\Users\yanbi\Desktop\Sum_Research\STAGE3-SPLIT_by_Quarters\Frequency.csv","a",encoding="utf8")
    outFile.writelines("\n")
    outFile.writelines(file_name_list[file_name_list_i][118:127])
    outFile.writelines("CAT"+str(cat)+" PART1 :")
    outFile.close()

    for i in range(5):
        t_tweets_ori = open(file_name_list[file_name_list_i],"r", encoding="utf8")
        current_word= words_set1[i]
        for ii in range (tweets_ori_rows):    
            tweets_ori_info = t_tweets_ori.readline()
            split_tweets_ori_info=tweets_ori_info.split(",")

            for j in range (len(split_tweets_ori_info)):
                c=split_tweets_ori_info[j]
                if (current_word==c):
                    num_of_word=num_of_word+1
                if (len(c)>1):
                    total_words=total_words+1

        # output
        ratio=num_of_word/total_words
        outFile = open(r"C:\Users\yanbi\Desktop\Sum_Research\STAGE3-SPLIT_by_Quarters\Frequency.csv","a",encoding="utf8")
        outFile.writelines("\n")
        outFile.writelines(current_word+","+str(num_of_word)+","+str(total_words)+","+str(ratio))
        outFile.close()
        num_of_word=0
        total_words=0

    # part2
    outFile = open(r"C:\Users\yanbi\Desktop\Sum_Research\STAGE3-SPLIT_by_Quarters\Frequency.csv","a",encoding="utf8")
    outFile.writelines("\n")
    outFile.writelines(file_name_list[file_name_list_i][118:127])
    outFile.writelines("CAT"+str(cat)+" PART2 :")
    outFile.close()

    for i in range(5):
        t_tweets_ori = open(file_name_list[file_name_list_i],"r", encoding="utf8")
        current_word= words_set2[i]
        for ii in range (tweets_ori_rows):    
            tweets_ori_info = t_tweets_ori.readline()
            split_tweets_ori_info=tweets_ori_info.split(",")

            for j in range (len(split_tweets_ori_info)):
                c=split_tweets_ori_info[j]
                if (current_word==c):
                    num_of_word=num_of_word+1
                if (len(c)>1):
                    total_words=total_words+1

        # output
        ratio=num_of_word/total_words
        outFile = open(r"C:\Users\yanbi\Desktop\Sum_Research\STAGE3-SPLIT_by_Quarters\Frequency.csv","a",encoding="utf8")
        outFile.writelines("\n")
        outFile.writelines(current_word+","+str(num_of_word)+","+str(total_words)+","+str(ratio))
        outFile.close()
        num_of_word=0
        total_words=0


t_tweets_ori.close()
