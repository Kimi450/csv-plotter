import os

rawCsvDir = os.getcwd() + "/raw-csv"
processedCsvDir = os.getcwd() + "/processed-csv"

for file in os.listdir(rawCsvDir):
    if not file.endswith(".csv"):
        continue
    with open(rawCsvDir+"/"+file,"r") as inFile, \
         open(processedCsvDir+"/processed_"+file,"w") as outFile:
        prevDate=None
        for line in inFile:
            line = line.split(",")
            if line[0]!="" and line[0] != prevDate:
                # put in the prevDate date where date wasnt present
                if "Date" in line[0]:
                    line[0]="Date"
                prevDate=line[0]
            line[0]=prevDate
            outFile.write(",".join(line))
