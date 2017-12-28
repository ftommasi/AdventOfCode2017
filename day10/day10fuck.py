thelist=[i for i in range(256)]
#thelist=[*range(5)]
position=0
#lengths=[97,167,54,178,2,11,209,174,119,248,254,0]
lengths = [225,171,131,2,35,5,0,13,1,246,54,97,255,98,254,110]
#lengths=3,4,1,5
skipsize=0

for length in lengths:
  # reverse the order
  temp=[]
  for temp_source in range(position,position+length):
    temp.append(thelist[temp_source%len(thelist)])
    #print(temp)
  for temp_counter in range(length):
    thelist[(position+temp_counter)%len(thelist)]=temp[-temp_counter-1]
  position=position+length+skipsize
  position=position%256
  skipsize+=1
#print (thelist)
print (thelist[0]*thelist[1])        
