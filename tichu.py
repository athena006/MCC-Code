def longest_run(N, K, cards):
  cards.sort()
  count = {}
  for card in cards:
      count[card] = count.get(card, 0) + 1

  longest_run = 0

  for card in cards:
      current_run = 0
      j = K

      while card in count and count[card] > 0:
          current_run += 1
          count[card] -= 1
          card += 1
          while j > 0 and card not in count:
              current_run += 1
              j -= 1
              card += 1

      longest_run = max(longest_run, current_run)

  return longest_run

# Read input values from a file
with open("lol.txt", "r") as file:
  N, K = map(int, file.readline().strip().split()[:2])
  cards = list(map(int, file.readline().split()))

result = longest_run(N, K, cards)
print("Longest run length:", result)
