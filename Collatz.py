question = input("Question: ")

string = question.split()

numbers = [float(num) for num in string]

repeat = int(input("Repeat for: "))

for i in range(repeat):
  new_numbers = []
  for num in numbers:
    if num % 2 == 0:
      new_numbers.append(num / 2.0)
    else:
      new_numbers.append(num * 3.0 + 1.0)
  numbers = new_numbers

print(sum(numbers))



