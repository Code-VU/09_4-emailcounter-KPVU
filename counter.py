def countEmail():
    # This first line is provided for you
    name = input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    handle = open(name)
    FromDict = {}
    for line in handle:
        StrippedLine = line.strip()
        if StrippedLine.startswith("From "):
            sender = StrippedLine.split()[1]
            if sender not in FromDict:
                FromDict[sender] = 1
            else:
                FromDict[sender] +=1
    DictValues = FromDict.values()
    MaxValue = max(DictValues)
    print(max(FromDict, key = FromDict.get), MaxValue) #key? not quite following the key part
## if you want to test locally run > python counter.py
if __name__ == "__main__":
    countEmail()
