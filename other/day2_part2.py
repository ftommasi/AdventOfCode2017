inputText = open("day2_part1_in.txt","r")
checksum = 0
for line in inputText:
  tempintList = map(int,line.split())
  tempintList.sort()
  intList = tempintList[::-1]
  i = 0
  j = 0
  while i < len(intList):
    j = i + 1
    while j < len(intList):
      if intList[i] % intList[j] == 0:
        checksum += (intList[i] / intList[j])
      j += 1
    i += 1  

print checksum
