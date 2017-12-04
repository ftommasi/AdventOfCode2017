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



