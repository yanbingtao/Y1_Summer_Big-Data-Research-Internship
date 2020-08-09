import csv
import operator
import math as math
import datetime
import glob

# path=r"C:\Users\yanbi\Desktop\newsData\Level3Data_combined"
# filename= path+"\All_"+prov+".csv"
filepath = r"C:\Users\yanbi\Desktop\newsData\all2_removeContent.csv"
countiesPath= r"C:\Users\yanbi\Desktop\newsData\UniqueAllCountiesName.csv"
outfilepath=r"C:\Users\yanbi\Desktop\newsData\output.csv"

rows, cols = (1969*127, 5) 
res = [[0 for i in range(cols)] for j in range(rows)]
res_count = [[0 for i in range(cols)] for j in range(rows)]

datafile=open(filepath,"r",encoding="utf8")
rows = 0
for row in datafile:
    rows += 1   


###!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
datafile=open(filepath,"r",encoding="utf8")
for row_i in range(rows):
    if row_i == 0:
        currentRow = datafile.readline()
    if row_i != 0:
        currentRow = datafile.readline()
        splitRowInfo=currentRow.split(",")
        
        current_county=splitRowInfo[1]
        current_date=splitRowInfo[5]
        current_cat=splitRowInfo[2]
        
        try: 
            current_datete_yyyy=current_date[0:4]
            current_datete_mm=current_date[4:6]
            if int(current_datete_yyyy)<2010:
                current_datete_yyyy="2010"
                current_datete_mm="01"
            data_position_row1=(int(current_datete_yyyy)-2010)*12+int(current_datete_mm)
            
            county_index_final=-1
            
            countiesfile=open(countiesPath,"r",encoding="utf8")
            for county_i in range(1969):
                currentRow_countie = countiesfile.readline()
                splitRowInfo_countie=currentRow_countie.split(",")
                
                counties_index=splitRowInfo_countie[0]
                counties_name=splitRowInfo_countie[1][:-1]
                
                if current_county==counties_name:
                    county_index_final=int(counties_index)
                    break
            
            if current_cat=='反腐':
                data_position_col=0
            elif current_cat=='党建':
                data_position_col=1
            elif current_cat=='倡廉':
                data_position_col=2
            elif current_cat=='投资':
                data_position_col=3
            elif current_cat=='招商':
                data_position_col=4
            
            if county_index_final!=-1:
                data_position_row=data_position_row1+county_index_final*127-1
                res_count[data_position_row][data_position_col] = res_count[data_position_row][data_position_col]+1
        except:
            continue
         
###!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#print out
# Print first row: 
outFile = open(outfilepath,"a",encoding="utf-8-sig")
output="County,Time,Num_Fanfu_news,Num_Dangjian_news,Num_Changlian_news,Num_Touzi_news,Num_Zhaoshang_news"
output+="\n"
outFile.writelines(output)
outFile.close()

outFile = open(outfilepath,"a",encoding="utf-8-sig")
countiesfile=open(countiesPath,"r",encoding="utf-8-sig")

for county_i in range (1969):
    currentRow_countie = countiesfile.readline()
    splitRowInfo_countie=currentRow_countie.split(",")
    counties_name=splitRowInfo_countie[1][:-1] #!!!

    yymmfile=open(r"C:\Users\yanbi\Desktop\newsData\yymm.csv","r")
    for month_i in range (127):
        output=""
        currentRow_yymm = yymmfile.readline()
        currentRow_yymm =currentRow_yymm[:-1] #!!!

        
        output=counties_name+","+currentRow_yymm+","+str(res_count[127*county_i+month_i][0])+","+str(res_count[127*county_i+month_i][1])+","+str(res_count[127*county_i+month_i][2])+","+str(res_count[127*county_i+month_i][3])+","+str(res_count[127*county_i+month_i][4])
        output+="\n"

        outFile.writelines(output)

print("done")