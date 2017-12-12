import operator
inputText = open("day8in","r")
#inputText = open("day8ex","r")
registers = {}
currentMax = -1
for line in inputText:
  splitLine = line.split()
  register = splitLine[0].strip()
  instruction = splitLine[1].strip()
  changeValue = splitLine[2].strip()
  targetRegister = splitLine[4].strip()
  condition = splitLine[5].strip()
  compareValue = splitLine[6].strip()
  print registers
  if register not in registers:
    registers[register] = 0
  if targetRegister not in registers:
    registers[targetRegister] = 0
  
  modifier = 1
  if "dec" in instruction:
    modifier = -1
  
  #print "register:", "\'"+register+"\'", "(", registers[register], ")"
  #print "instruction:", instruction
  #print "changeValue:", changeValue
  #print "modifier:", modifier
  #print "targetRegister:", "\'"+targetRegister+"\'", "(", registers[targetRegister], ")"
  #print "condition:", condition
  print "compareValue:", compareValue
  

  
  if "!=" in condition:
    if registers[targetRegister] != int(compareValue):
      #print "computing:", register, "=", registers[register], "+", (modifier * int(changeValue)), "(", registers[register] + (modifier * int(changeValue)), ")"
      registers[register] = registers[register] + (modifier * int(changeValue))
  
  elif "==" in condition:
    if registers[targetRegister] == int(compareValue):
      #print "computing:", register, "=", registers[register], "+", (modifier * int(changeValue)), "(", registers[register] + (modifier * int(changeValue)), ")"
      registers[register] = registers[register] + (modifier * int(changeValue))

  elif ">=" in condition:
    if registers[targetRegister] >= int(compareValue):
      #print "computing:", register, "=", registers[register], "+", (modifier * int(changeValue)), "(", registers[register] + (modifier * int(changeValue)), ")"
      registers[register] = registers[register] + (modifier * int(changeValue))

  elif "<=" in condition:
    if registers[targetRegister] <= int(compareValue):
      #print "computing:", register, "=", registers[register], "+", (modifier * int(changeValue)), "(", registers[register] + (modifier * int(changeValue)), ")"
      registers[register] = registers[register] + (modifier * int(changeValue))

    
  elif ">" in condition:
    if registers[targetRegister] > int(compareValue):
      #print "computing:", register, "=", registers[register], "+", (modifier * int(changeValue)), "(", registers[register] + (modifier * int(changeValue)), ")"
      registers[register] = registers[register] + (modifier * int(changeValue))

  
  elif "<" in condition:
    if registers[targetRegister] < int(compareValue):
      #print "computing:", register, "=", registers[register], "+", (modifier * int(changeValue)), "(", registers[register] + (modifier * int(changeValue)), ")"
      registers[register] = registers[register] + (modifier * int(changeValue))


  #print registers

  #print "------------------------"
  #print ""
  
  maxKey = max(registers.iteritems(), key=operator.itemgetter(1))[0]
  if registers[maxKey] > currentMax:
    currentMax = registers[maxKey]

print currentMax
