import sys

input = sys.stdin.readline

n = int(input())
f_line = list(map(int, input().split()))
f_line.sort()

s_line = list(map(int, input().split()))
s_line.sort(reverse=True)

result = 0
for n in range(len(f_line)):
    result += f_line[n] * s_line[n]
print(result)
