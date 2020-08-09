import csv
import glob

path =r"C:\Users\yanbi\Desktop\Sum_Research2\National data"
fileNameList = glob.glob(path+"/*.csv")

for file in fileNameList: 
    ###Count rows in the file 
    currentFile = open(file,"r", encoding="utf8")
    rows = 0
    for row in currentFile:
        rows += 1

    ###reopen the file to iterate every rows
    currentFile = open(file,"r", encoding="utf8")

    ### Print title:
    output = ('留言标题,留言类别1,留言类别2,留言时间,留言内容\n')
    output_name=path+"\ALL_National.csv"
    outFile = open(output_name,"a",encoding="utf8")
    outFile.writelines(output)
    outFile.close()

    for i in range(rows):
        currentRow = currentFile.readline()
        splitRowInfo=currentRow.split(",")

        
        try:
            output=""
            if i==0:
                # do nothing
                a=0
            else:
                output = (splitRowInfo[6]+","+splitRowInfo[8]+","
                            +splitRowInfo[9]+","
                            +splitRowInfo[10][0:4]+splitRowInfo[10][5:7]+splitRowInfo[10][8:10]
                            +","+splitRowInfo[11]+"\n")

            # output = (splitRowInfo[2]+","+splitRowInfo[3]+","
            #             +splitRowInfo[4]+","+splitRowInfo[5]+","
            #             +splitRowInfo[6]+","+splitRowInfo[8]+","
            #             +splitRowInfo[9]+","+splitRowInfo[10]+","
            #             +splitRowInfo[11]+","+splitRowInfo[12]+","
            #             +splitRowInfo[13]+","+splitRowInfo[14]+"\n")

            ### filter out nonsignificant words
            # for jj in range (len(out_str)):
            #     char = out_str[jj]
            #     if (char=="/" or char=='<' or char=='>' or (char>="0" and char<="9") or (char>="a" and char<="z") or char=='=' or char=='&' or char=='%' or (char>="A" and char<="Z")
            #     or char=="！"or char=="《" or char=="》" or char=="…" or char=="?" or char=="." or char=="年" or char==";" or char=="月" or char=="日" or char=="的" or char==":" or char==";"
            #     or char=="#"
            #     or char=="-" or char=="。" or char=="，"or char=="[" or char=="]" or char=="_"):
            #         out_str=out_str.replace(char," ")
            # out_str=out_str.replace(" ","")

                output_name=path+"\ALL_National.csv"
                outFile = open(output_name,"a",encoding="utf8")
                outFile.writelines(output)
                outFile.close()
        except:
            continue

        
               


print("done!")