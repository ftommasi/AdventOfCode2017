inputFile = open("day6input","r")
#inputFile = open("day6ex","r")
banks = None
#only one line
for line in inputFile:
  banks = map(int,line.split())
seen = {}
cycles = 0
while tuple(banks) not in seen:
  maxIndex = banks.index(max(banks))
  toDistribute = banks[maxIndex]
  i = (maxIndex + 1) % len(banks)
  while toDistribute > 0:
    banks[i] += 1
    toDistribute -=1;
    i = (i + 1)%len(banks)
  cycles += 1
  seen[tuple(banks)] = 1
  #print seen
print cycles
