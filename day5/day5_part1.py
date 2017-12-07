filein = open("day5input","r")
#filein = open("day5inputtest","r")
instructions = []
for line in filein:
  instructions.append(int(line))
stepsTaken = 0
currentIndex = 0
nextIndex =  0 #instructions[currentIndex] + currentIndex
while True:
  try:
    prevIndex = currentIndex
    nextIndex = instructions[currentIndex] + currentIndex 
    currentIndex = nextIndex
    instructions[prevIndex] += 1
    if currentIndex > len(instructions) or currentIndex < 0:
      break
    else:
      stepsTaken += 1
  except:
    break
print stepsTaken
 

