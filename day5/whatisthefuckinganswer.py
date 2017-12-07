def count_maze_exit_steps(input_list):
  count = 0
  index = 0
  while index >= 0 and index < len(input_list):
    change = input_list[index]
    input_list[index] += 1
    index += change
    count += 1
  return count

with open("day5input2", 'r') as input_file:
  input_numbers = [int(line) for line in input_file]
print(count_maze_exit_steps(input_numbers))
