
import random

class ClassGroups:

    """ This class is for creating groups from a list of members to ensure
    true random selection of group members when doing activities. """
    
    def __init__(self):

        self.file = "members.txt"
        self.numberOfGroups = 6
        self.groupList = []
        self.randGroups = []

        ##methods

        self.loadMembers()
        self.shuffleMembers()
        self.createRandGroups()
        self.createGroups()

        for group in self.randGroups:
            print(group)
            print()


    def loadMembers(self):

       
        with open(self.file, mode="r",encoding="utf-8") as myFile:
            for line in myFile:
                newName = line.rstrip("\n")
                self.groupList.append(newName)

    def shuffleMembers(self):
        
        random.shuffle(self.groupList)

    def createGroups(self):
        
        done = False
        ##populate group list
        while done != True or len(self.groupList) != 1:
            try:
                for i in range(0,self.numberOfGroups):
                        temp = self.groupList[0]
                        self.groupList.pop(0)
                        self.randGroups[i].append(temp)
            except IndexError:
                break

    def createRandGroups(self):
        for i in range(1,self.numberOfGroups + 1):
            
            newGroup = []

            self.randGroups.append(newGroup)
        
        
        

if __name__ == "__main__":

    Calc = ClassGroups()

    
    
