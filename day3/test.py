import math
number_to_test= input()

first_try = int(math.sqrt(number_to_test))+1
if first_try % 2 == 0:
  print (first_try + 1) * (first_try + 1)
else:
  print first_try * first_try
