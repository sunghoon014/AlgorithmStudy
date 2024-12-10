import sys

input = sys.stdin.read
data = input().splitlines()
N = int(data[0])

coordinates = []
for i in range(1, N + 1):
    x = int(data[i].split()[0])
    y = int(data[i].split()[1])
    coordinates.append([x, y])

coordinates.sort(key=lambda x: (x[0], x[1]))

for x, y in coordinates:
    print(x, y)