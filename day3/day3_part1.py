import math
target = input()
grid_sqrt = int(math.sqrt(target))+1
grid_size = 1
row_col_size = 1
distance = 0
if grid_sqrt % 2 == 0:
  grid_size = ((grid_sqrt+ 1) * (grid_sqrt+ 1))
  row_col_size = grid_sqrt + 1
else:
  grid_size = (grid_sqrt*grid_sqrt)
  row_col_size = grid_sqrt

corners = []
step_size = row_col_size - 1
for i in xrange(4):
  corners.append( (grid_size - i*(step_size)) - row_col_size/2 )

distances =[]
for i in corners:
  distances.append(abs(i-target))

distance += row_col_size/2
distance += min(distances)
print distance 




