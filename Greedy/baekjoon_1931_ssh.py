import sys

input = sys.stdin.read
data = input().splitlines()
n = int(data[0])

timetable = []

for i in range(1, n + 1):
    start, end = map(int, data[i].split())
    timetable.append([start, end])

timetable.sort(key=lambda x: (x[1], x[0]))

nowend = 0
ans = 0
for start, end in timetable:
    if nowend <= start:
        ans += 1
        nowend = end
print(ans)