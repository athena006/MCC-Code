total = int(input("Total number of cards: "))
w = int(input("Wildcards: "))
n = total - w
question = input("Question:  ")
numbers = [int(num) for num in question.split()]
numbers.sort()
count = 1
longest = 1

for i in range(1, n):
  diff = numbers[i] - numbers[i - 1] 
  if diff == 0:
    continue
  if diff * (i - 1) <= w:
    count += diff * (i - 2)
    w -= diff 
  if count > longest:
    longest = count
  
longest = count + w - 1

print("Longest run length:", longest)
