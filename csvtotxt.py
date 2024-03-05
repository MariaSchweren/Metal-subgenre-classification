CompleteLinkList = open("Linklist.txt", "w")
LinkList = open("List.csv")

for line in LinkList:
    line = line.rstrip("\n")
    lineArray = line.split(";")[1:]
    for entry in lineArray:
        if entry != "":
            CompleteLinkList.write(entry + "\n")