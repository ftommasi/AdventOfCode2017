inputText = open("day7input","r")
withChildren = []
parentChild = {}
nodeWeight = {}
for l in inputText:
  line = l.strip()
  splitLine = line.split("->")
  parent = splitLine[0].split()[0]
  weight = splitLine[0].split()[1].strip("()")
  child = None
  if len(splitLine) > 1:
    child = splitLine[1].strip(" ").split(", ")

  if "->" in line:
    withChildren.append(line)
    parentChild[parent] = child
    nodeWeight[parent] = weight
print "done"
