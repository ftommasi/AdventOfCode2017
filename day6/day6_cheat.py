import itertools

inputFile = open("day6input","r")
banks = None
for line in inputFile:
  banks = [int(x) for x in line.split()] 
seen = {}
cycles = 0
lastPattern = None
print(banks)

while True:
#while tuple(banks) not in seen:
  seen[tuple(banks)] = cycles
  i,m = max(enumerate(banks),key = lambda k: (k[1], -k[0]))
  banks[i] = 0
  for j in itertools.islice(itertools.cycle(range(len(banks))), i + 1, i + m + 1):
    banks[j] += 1
  cycles += 1
  if tuple(banks) in seen:
    lastPattern = tuple(banks)
    break    	
print(cycles - seen[lastPattern])
