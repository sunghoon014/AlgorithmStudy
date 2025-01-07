winner, max = 0, 0
for i in range(1, 6):
    score = sum(map(int, input().split()))
    if max<score:
        winner = i
        max = score

print(winner, max)