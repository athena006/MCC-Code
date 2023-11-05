file_name = input("File: ")

numbers = []
with open(file_name, 'r') as file:
  for line in file:
    line_numbers = [int(num) for num in line.split()]
    numbers.extend(line_numbers)

highest = 0
greatest = 0
group = ""
new = ""
total = 0
card_values = len(numbers) / 4
cards = int(input("Number of cards required: "))

for i in range(0, len(numbers), 4):
  x = sum(numbers[i:i+4])
  if x > highest:
    highest = x
    group = i

print("Highest value of card:", highest)

del numbers[int(group):int(group)+4]
total = highest

for z in range(cards - 1):
  greatest = 0
  for j in range(0, len(numbers), 4):
    y = sum(numbers[j:j+2])
    if y > greatest:
      greatest = y
      new = j
  del numbers[int(new):int(new)+4]
  total += greatest

print("Total card values:", total)


