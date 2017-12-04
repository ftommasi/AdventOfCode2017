numString = raw_input()
sumResult = 0
if numString[0] == numString[len(numString) -1]:
  sumResult += int(numString[0])
for i in xrange(len(numString) - 1):
  currentDigit = numString[i]
  nextDigit = numString[i +1]
  if currentDigit == nextDigit:
    sumResult += int(currentDigit)

print sumResult
