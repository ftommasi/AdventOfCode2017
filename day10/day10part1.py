def getSublistFromCircular(fullList, startIndex, endIndex):
  if startIndex < endIndex:
    return fullList[startIndex:endIndex]
  else:
    return fullList[endIndex:] + fullList[:startIndex]

def replaceSublist(original,toCopy,startIndex):
  for i in xrange(len(toCopy)):
    original[(startIndex + i)%len(original)] = toCopy[i] 
  return original



inputList = [225,171,131,2,35,5,0,13,1,246,54,97,255,98,254,110]
knotSize = 256

#inputList = [3,4,1,5]
#knotSize = 5

knot = [i for i in xrange(knotSize)]

startIndex = 0
skipSize = 0
for number in inputList:
  endIndex = (startIndex + number) % len(knot)
  temp = getSublistFromCircular(knot,startIndex,endIndex)
  reverse = temp[::-1]
  knot = replaceSublist(knot,reverse,startIndex)
  startIndex = (startIndex + number + skipSize - 1) % len(knot)
  skipSize += 1
  '''
  print""
  print"----------------"
  print knot
  print"----------------"
  print ""
  '''

print knot
print knot[0] * knot[1]

