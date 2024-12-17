import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort(reverse=True)

time = 0
for i, j in enumerate(data):
    time += (i+1)*j

print(time)