inputText = open("day2_part1_in.txt","r")
checksum = 0
for line in inputText:
  intList = map(int,line.split())
  currMax = max(intList)
  currMin = min(intList)
  checksum += (currMax - currMin)
print checksum
