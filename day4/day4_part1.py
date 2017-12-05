inputText = open("day4input","r")
valid = 0 
for line in inputText:
  found = []
  valid += 1
  for w in line.split():
    word = "".join(sorted(w))
    if word not in found:
      found.append(word)
    else:
      valid -= 1
      break

print valid


