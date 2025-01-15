import sys
input = sys.stdin.readline

n = int(input())
castle = list(map(int, input().split()))

stack, result = [], []
for i in range(n):
    while stack and stack[-1][1]<castle[i]:
        stack.pop()
    if stack:
        result.append(stack[-1][0])
    else:
        result.append(0)
    stack.append((i+1, castle[i]))

print(*result)