target = input()
topLeft = 4
topRight = 2
botLeft = 1
botRight = 1
lastAdded = topLeft
i = 4
while True:
  #shiftLeft
  topRight = topLeft
  botRight = botLeft
  #addNumber
  topLeft = topRight + botRight
  lastAdded = topLeft
  if lastAdded > target:
    break
  #addNumber
  botLeft = topRight + topLeft + botRight
  lastAdded = botLeft
  if lastAdded > target:
    break
  #shift Down
  topLeft = botLeft
  topRight = botRight

  #add Number
  botLeft = topRight + topLeft
  lastAdded = botLeft
  if lastAdded > target:
    break
  #add Number
  botRight = topRight + topLeft + botLeft
  lastAdded = botLeft
  if lastAdded > target:
    break
  

print lastAdded
