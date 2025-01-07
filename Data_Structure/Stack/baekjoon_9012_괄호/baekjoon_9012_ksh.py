import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    PS = input().strip()
    stack = []
    for p in PS:
        if p == "(":
            stack.append(p)
        else:
            if stack:
                stack.pop()
            else:
                stack.append(p)
                break
    if stack:
        print("NO")
    else:
        print("YES")
