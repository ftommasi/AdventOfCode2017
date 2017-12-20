inputFile = open("day9in","r")
ignore = False
garbage = False
modifier = 0
total = 0
garbageCount = 0
for string in inputFile: #only one loop iteration
  for char in string:
    if not ignore:
      if not garbage:
        if "{" in char:
          modifier += 1
        elif "}" in char:
          total += modifier
          modifier -=1
        elif "<" in char:
          garbage = True
      else:
        if ">" in char:
          garbage = False
        elif "!" in char:
          ignore = True
        else:
          garbageCount += 1

    else:
      ignore = False
        

print garbageCount
