inputFile = open("day6input","r")
#inputFile = open("day6ex","r")
banks = None
#only one line
for line in inputFile:
  banks = map(int,line.split())
seen = {}
t_banks = None
cycles = 0
while True:
  #print "before redist", banks
  maxIndex = banks.index(max(banks))
  toDistribute = banks[maxIndex]
  i = (maxIndex + 1) % len(banks)
  while toDistribute > 0:
    banks[i] += 1
    toDistribute -=1;
    i = (i + 1)%len(banks)
  #print "after redist", banks
  t_bank = tuple(banks)
  cycles += 1
  if t_banks in seen:
    #print "breaking"
    break
  
  seen[t_banks] = 1
  #print seen
print cycles
