question = input("Enemy power levels: ")
string = question.split()
levels = [int(num) for num in string]
initial = int(input("Initial power level: "))
test = initial
final = int(input("Power level Alice needs to reach: "))
levels_1 = []
enemy_count = 0

for i in range(len(levels)):
  test += levels[i]
if test < final:
  print(-1)
else:
  while initial < final:
    max_power = max(levels)
    while max_power >= initial:
      levels_1.append(max_power)
      levels.remove(max_power)
      max_power = max(levels)
    if max_power < initial:
      initial += max_power
      levels.remove(max_power)
      enemy_count += 1
    levels.extend(levels_1)
    levels_1 = []

print(enemy_count)
