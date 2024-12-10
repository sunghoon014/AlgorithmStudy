import sys
N = int(sys.stdin.readline())
total = []
for _ in range(N):
    x, y = sys.stdin.readline().strip().split()
    total.append([int(x), int(y)])

for item in sorted(total, key=lambda x: (x[0], x[1])):
    print(item[0], item[1])