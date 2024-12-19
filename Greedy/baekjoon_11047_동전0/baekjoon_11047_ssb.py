import sys
input = sys.stdin.readline
n, k = map(int, input().split())

stack = []
for _ in range(n):
    data = int(input())
    if data <= k:
        stack.append(data)

cnt = 0
while k != 0:
    money = stack.pop()
    cnt += k // money
    rest = k % money
    k = rest

print(cnt)