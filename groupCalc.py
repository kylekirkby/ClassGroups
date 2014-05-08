


randGroups = []

numberOfGroups = 5


groupList = []
with open("members.txt",mode="r",encoding="utf-8") as myFile:
        for line in myFile:
                newName = line.rstrip("\n")
                groupList.append(newName)
        
print(groupList)
numberOfStudents = len(groupList)
####create student list
##for i in range(1,numberOfStudents + 1):
##    groupList.append(i)

##create group list
for i in range(1,numberOfGroups + 1):
    
    newGroup = []

    randGroups.append(newGroup)


done = False
##populate group list
while done != True or len(groupList) != 1:
    
    for i in range(0,numberOfGroups):
            temp = groupList[0]
            groupList.pop(0)
            randGroups[i].append(temp)
        
   

        
