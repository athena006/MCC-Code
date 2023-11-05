file = input("File: ")
numbers = []
with open(file, 'r') as file:
  for line in file:
    line_numbers = [int(num) for num in line.split()]
    numbers.extend(line_numbers)

rows = len(numbers) // 4
columns = 4
groups = [[0 for j in range(columns)] for i in range(rows)]
for i in range(rows):
  for j in range(columns):
    groups[i][j] = numbers[i * 4 + j]
print(groups)
highest = 0
total = 0
for i in range(rows - 3):
  for j in range(columns - 3):  
    x = sum(groups[i][j:j+4])
    if x > highest:
      highest = x
      index = (i, j)
print("Highest Sum:", highest)
del groups[i]
total += highest
repeat = int(input("How many cards are needed? "))

for z in range(repeat-1):
    greatest = 0
    index = (0, 0)  
    for i in range(rows - 1):
        for j in range(columns - 1):
            if j+2 >= columns:
                break
            y = sum(groups[i][j:j+2])
            if y > greatest:
                greatest = y
                index = (i, j)
    total += greatest
    i, j = index  
    del groups[i]
print("Total:", total)
