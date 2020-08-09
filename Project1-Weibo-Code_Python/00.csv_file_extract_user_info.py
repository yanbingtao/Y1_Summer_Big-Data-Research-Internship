import csv

# //read  
# with open(r"C:\My Files\VS Code\Python\test1.csv","r") as file1:
#     reader1 = csv.reader(file1)
#     uni = reader1
#     for row1 in reader1:
#         print(row1)

# //write 
# with open(r"C:\My Files\VS Code\Python\test1.csv","a") as file_w:
#     writer = csv.writer(file_w)
#     writer.writerow([1,2,3,4,5])
 
# //copy file1 to file 2     http://beancoder.com/csv-files-using-python/
# with open(r"C:\My Files\VS Code\Python\test2.csv","w") as file_w:
#     fileWriter = csv.writer(file_w)
#     with open(r"C:\My Files\VS Code\Python\test1.csv",'r') as inFile:
#         fileReader = csv.reader(inFile)
#         for row in fileReader:
#             fileWriter.writerow(row)


# https://stackoverflow.com/questions/54360132/outer-for-loop-execute-only-once-in-python
# with open(r"C:\My Files\VS Code\Python\test2.csv","w") as outFile:
#     fileWriter = csv.writer(outFile)
#     with open(r"C:\My Files\VS Code\Python\test1.csv",'r') as inFile1:
#         fileReader1 = csv.reader(inFile1)
#         with open(r"C:\My Files\VS Code\Python\test.csv",'r') as inFile0:
#             fileReader0 = csv.reader(inFile0)

#             for row0 in fileReader0:
#                 for row1 in fileReader1:
#                         # if row0!=row1: fileWriter.writerow(row1)
#                     print ("0: ",r0, " // 1: ", row1)
#                         # continue


# i=[1,2,3]
# j=["a","b","c"]
# for ii in i:
#     for jj in j:
#         print(ii,jj)

# // https://stackoverflow.com/questions/38996033/python-compare-two-csv-files-and-print-out-differences


# import csv
# t1500 = open(r"C:\Users\yanbi\Desktop\Sum_Research\sample_1500users.csv","r",encoding="utf8")
# t1000 = open(r"C:\Users\yanbi\Desktop\Sum_Research\users1000fs.csv","r",encoding="utf8")
# file_1500 = t1500.readlines()
# file_1000 = t1000.readlines()
# t1500.close()
# t1000.close()

# outFile = open(r"C:\My Files\VS Code\Python\test2.csv","w")

# for i in file_1000:
#     if len(i) !=0:
#         split_i=i.split(",")
#         for j in file_1500:
#             if len(j) !=0:
#                 split_j=j.split(",")
#                 if (split_i[0] == split_j[5]):
#                     outFile.write(i)

# outFile.close()




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

# t1000 = open(r"C:\My Files\VS Code\Python\test.csv","r")
t1000 = open(r"C:\Users\yanbi\Desktop\Sum_Research\users1000fs.csv","r",encoding="utf8")

for i in range (t):
    file_1000 = t1000.readline()

for i in range (num_rows_1000):
    file_1000 = t1000.readline()
    split_1000=file_1000.split(",")
    t1500_1 = open(r"C:\Users\yanbi\Desktop\Sum_Research\sample_1500users.csv","r",encoding="utf8")
    file_1500 = t1500_1.readline()
    # t1500_1 = open(r"C:\My Files\VS Code\Python\test1.csv","r")
    
    for j in range (num_rows_1500):
        file_1500 = t1500_1.readline()
        split_1500=file_1500.split(",")
        if (len(split_1000)>0 and len(split_1500)>5):
            try:
                str1=int(split_1000[0][1:-1])
                str2=int(split_1500[5])
                if (str1 == str2):
                    out_str=""
                    for k in range(len(split_1000)):
                        if k !=len(split_1000)-1:
                            out_str+=split_1000[k]+","
                        else:
                            out_str+=split_1000[k]
                    outFile.writelines(out_str)
            except:
                continue
    t1500_1.close()

t1000.close()
t1500.close()
outFile.close()
                    




