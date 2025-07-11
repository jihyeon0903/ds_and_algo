""" Describe how the built-in sum function can be combined with Python's comprehension syntax to compute the sum of all numbers in an nxn data set, represented as a list of lists """

def sum_of_all_numbers(grid):
  summed = sum([sum(row) for row in grid])
  return summed

n = 10
grid = []
for i in range(n):
  row = []
  grid.append(row)
  for j in range(n):
    row.append(j)

print(sum_of_all_numbers(grid))