import os

rawCsvDir = os.getcwd() + "/raw-csv"
processedCsvDir = os.getcwd() + "/processed-csv"

for file in os.listdir(rawCsvDir):
    if not file.endswith(".csv"):
        continue
    try:
        inFile = open(rawCsvDir+"/"+file,"r")
        outFile = open(processedCsvDir+"/processed_"+file,"w")
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
    except Exception as e:
        print(e)
        string = "Error opening file '{}'.".format(file)
        print(string)
        continue
    finally:
        try:
            inFile.close()
            outFile.close()
        except:
            pass
