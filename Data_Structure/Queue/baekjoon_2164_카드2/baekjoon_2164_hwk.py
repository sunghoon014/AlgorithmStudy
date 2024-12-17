from collections import deque
n = int(input())
cards = deque(list(range(1, n+1)))

while len(cards) > 1:
    cards.popleft() # 제일 위에 있는 카드
    cards.append(cards.popleft())   # 제일 위에 있는 카드 맨 밑으로

print(cards.popleft())