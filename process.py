in = open("acc.csv","r")
out = open("processed_acc.csv","w")

prev=None
for line in in:
    line = line.split(",")
    print(line)
    if if line[0]!="" and line[0] != prev:
        prev=line[0]
    out.write()
