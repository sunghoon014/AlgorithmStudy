import sys

input = sys.stdin.read
data = input().splitlines()
N = int(data[0])

cards = {}
for i in range(1, N + 1):
    card = int(data[i])
    if card in cards:
        cards[card] += 1
    else:
        cards[card] = 1

cards_sort = sorted(cards.items(), key = lambda x: (-x[1], x[0]))
print(cards_sort[0][0])

