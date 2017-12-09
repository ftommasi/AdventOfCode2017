dataFile = open("day7input","r")
data = dataFile.read()
dataFile.close()

data = data.split("\n")


class program:

    def __init__(self,name,weight = 0):
        self.parent = None
        self.name = name
        self.weight = weight
        self.children = []

    def getRoot(self):
        if(self.parent == None):
            return self
        else:
            return self.parent.getRoot()

    def fix(self):
        #print(self.name)
        for i in range(len(self.children)):
            #print("\t"+self.children[i])
            self.children[i] = getProgramByName(self.children[i].replace(" ", ""))
            self.children[i].parent = self

    def getTotal(self):
        total = 0
        total += self.weight
        for child in self.children:
            total += child.getTotal()
        return total;

    def goodWeight(self):
        #only use post fix
        if(self.parent == None):
            return True
        if(len(self.parent.children) < 1):
            return True

        good = False
        for sib in self.parent.children:
            if(sib == self):
                continue
            if(sib.getTotal() == self.getTotal()):
                good = True

        if(not good):
            print("something is wrong with "+self.name)
            print("weight: "+str(self.weight))
            print("total weight: "+str(self.getTotal()))
            for sib in self.parent.children:
                if(sib == self):
                    continue
                else:
                    print(sib.name+"\tweight: "+str(sib.getTotal()))
        return good



programs = []
def getProgramByName(name):
    global programs
    for program in programs:
        if(program.name == name):
            return program
    return None



for line in data:
    name = line.split(" ")[0]
    name.strip()
    newP = program(name,
        int(
            line.split("(")[1].split(")")[0]
            )
        )

    if(len(line.split("->")) > 1):
        for pName in line.split("->")[1].split(","):
            pName.strip()
            newP.children.append(pName)


    programs.append(newP)

for program in programs:
    program.fix()

for program in programs:
    program.goodWeight()
