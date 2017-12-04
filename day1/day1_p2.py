numString = raw_input()
sumResult = 0
for i in xrange(len(numString) - 1):
  currentDigit = numString[i]
  nextDigit = numString[(i + len(numString)/2)%len(numString)]
  if currentDigit == nextDigit:
    sumResult += int(currentDigit)

print sumResult
