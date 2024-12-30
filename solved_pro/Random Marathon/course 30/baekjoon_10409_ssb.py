n, t = map(int, input().split())
data = list(map(int, input().split()))

i = 0
for d in data:
    t -= d
    if t<0:
        break
    i += 1

print(i)