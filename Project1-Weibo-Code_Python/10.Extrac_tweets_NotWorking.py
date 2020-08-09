# want to extract tweets from csv file, and sort them based on user,
# BUT NOT WORKING!! File too big

import csv
t1000 = open(r"C:\Users\yanbi\Desktop\Sum_Research\users1000fs.csv","r",encoding="utf8")
t1500 = open(r"C:\Users\yanbi\Desktop\Sum_Research\sample_1500users.csv","r",encoding="utf8")
# t1000 = open(r"C:\My Files\VS Code\Python\test.csv","r")
# t1500 = open(r"C:\My Files\VS Code\Python\test1.csv","r")
outFile = open(r"C:\My Files\VS Code\Python\test2.csv","w",encoding="utf8")


# num_rows_1000 = 0
# for row in t1000:
#     num_rows_1000 += 1

# num_rows_1500 = 0
# for row in t1500:
#     num_rows_1500 += 1

num_rows_1000=1757982
num_rows_1500=3419305
t=9831
t2=14960

# t1000 = open(r"C:\My Files\VS Code\Python\test.csv","r")
t1000 = open(r"C:\Users\yanbi\Desktop\Sum_Research\users1000fs.csv","r",encoding="utf8")

for i in range (t):
    file_1000 = t1000.readline()

t1500_1 = open(r"C:\Users\yanbi\Desktop\Sum_Research\sample_1500users.csv","r",encoding="utf8")
file_1500 = t1500_1.readline()
mem=t1500_1.readline()

for i in range (t2-t):
    file_1000 = t1000.readline()
    split_1000=file_1000.split(",")
    
    # t1500_1 = open(r"C:\My Files\VS Code\Python\test1.csv","r")
    
    split_mem=mem.split(",")
    try:
        str1=int(split_1000[0][1:-1])
        str2=int(split_mem[5])
        if (str1 == str2):
            # ===========================================
            for j in range (num_rows_1500):
                if (j==0):
                    file_1500=mem
                else:
                    file_1500 = t1500_1.readline()

                split_1500=file_1500.split(",")
                if (len(split_1000)>0 and len(split_1500)>7):
                    try:
                        str1=int(split_1000[0][1:-1])
                        str2=int(split_1500[5])
                        if (str1 == str2):
                            out_str=""
                            out_str = split_1500[5]+","+split_1500[6]+","+split_1500[7]+","+split_1500[4]+"\n"
                            outFile.writelines(out_str)
                        else: 
                            mem=file_1500
                            break
                    except:
                        continue
    except:
        continue




t1500_1.close()
t1000.close()
t1500.close()
outFile.close()