# extract tweets only for 107 group users, sorted

import csv
# t_user = open(r"C:\Users\yanbi\Desktop\Sum_Research\user107.csv","r",encoding="utf8")
old_file = open(r"C:\Users\yanbi\Desktop\Sum_Research\users1000fs_sum_cat_111.csv","r",encoding="utf8")
new_file = open(r"C:\Users\yanbi\Desktop\Sum_Research\users1000fs_sum_cat_all.csv","a",encoding="utf8")


# num_rows_1000 = 0
# for row in t_user:
#     num_rows_1000 += 1

num_rows_old = 0
for row in old_file:
    num_rows_old += 1

# num_rows_1000=6
# num_rows_1500=3417127

old_file = open(r"C:\Users\yanbi\Desktop\Sum_Research\users1000fs_sum_cat_111.csv","r",encoding="utf8")

for i in range(num_rows_old):
    # file_1000_user=t_user.renum_rows_1500dline()
    file_1500_tweets = old_file.readline()
    new_file.writelines(file_1500_tweets)



old_file.close()
new_file.close()