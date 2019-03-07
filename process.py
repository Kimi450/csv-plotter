inputFrom="acc.csv"
outputTo="processed_"+inputFrom

try:
    inFile = open(inputFrom,"r")
    outFile = open(outputTo,"w")
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
except:
    print("Error opening file(s), please try again.")
    exit()
finally:
    try:
        inFile.close()
        outFile.close()
    except:
        pass
