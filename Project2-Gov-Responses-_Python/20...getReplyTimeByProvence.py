import csv
import glob

path =r"C:\Users\yanbi\Desktop\Sum_Research2\National data ReplyTime"
fileNameList = glob.glob(path+"/*.csv")
path_output =r"C:\Users\yanbi\Desktop\Sum_Research2\RawData\ReplyTimeByCities"
output_name =path_output+"\ReplyTimeByCities.csv"
output_name_temp =path_output+"\Temp.csv"

### Print title:
output = ('省份,城市,区县,回复时间，\n')
outFile = open(output_name,"a",encoding="utf8")
outFile.writelines(output)
outFile.close()
### Create temp file:
outFile_temp = open(output_name_temp,"w",encoding="utf8")
outFile_temp.close()


for file in fileNameList: 
    ###Count rows in the file 
    currentFile = open(file,"r", encoding="utf8")
    rows = 0
    for row in currentFile:
        rows += 1

    ###reopen the file to iterate every rows
    currentFile = open(file,"r", encoding="utf8")

    for i in range(rows):
        currentRow = currentFile.readline()
        splitRowInfo=currentRow.split(",")
        
        try:
            date = int(splitRowInfo[4][0:4]+splitRowInfo[4][5:7]+splitRowInfo[4][8:10])
            output=""
            if i==0:
                # do nothing
                a=0
            elif(date<=20130101 and date>=20200530):
                a=2
            else:
                output = (splitRowInfo[1]+","+splitRowInfo[2]+","
                            +splitRowInfo[3]+","
                            +splitRowInfo[4][0:4]+splitRowInfo[4][5:7]+splitRowInfo[4][8:10]
                            +","+"\n")

                ### take earliest date, open-temp-file
                outFile_temp = open(output_name_temp,"r", encoding="utf8")
                rows_temp = 0
                for row in outFile_temp:
                    rows_temp += 1

                if rows_temp==0:
                    outFile_temp = open(output_name_temp,"w",encoding="utf8")
                    outFile_temp.writelines(output)
                    outFile_temp.close()
                else:
                    # compare who is the earliest for now
                    ## same city?
                    outFile_temp = open(output_name_temp,"r", encoding="utf8")
                    output_temp = outFile_temp.readline()
                    splitInputInfo=output_temp.split(",")

                    splitOutputInfo=output.split(",")
                    
                    if (splitInputInfo[0]==splitOutputInfo[0] and splitInputInfo[1]==splitOutputInfo[1] and splitInputInfo[2]==splitOutputInfo[2]):
                        # same city, compare who is the ealist.
                        if (int(splitInputInfo[3])>int(splitOutputInfo[3])):
                            output=splitOutputInfo[0]+","+splitOutputInfo[1]+","+splitOutputInfo[2]+","+splitInputInfo[3]+","+"\n"
                            # then update temp file
                            outFile_temp = open(output_name_temp,"w",encoding="utf8")
                            outFile.writelines(output)
                            outFile.close()
                    else: 
                        #different city, move temp file to output file, update temp file
                        outFile = open(output_name,"a",encoding="utf8")
                        outFile.writelines(output_temp)
                        outFile.close()
                        # then update temp file
                        outFile_temp = open(output_name_temp,"w",encoding="utf8")
                        outFile_temp.writelines(output)
                        outFile_temp.close()

                ### end-temp-file
        except:
            continue

        
               


print("done!")