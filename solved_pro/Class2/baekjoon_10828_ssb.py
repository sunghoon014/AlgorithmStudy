import sys
input = sys.stdin.readline
n = int(input())

stack = []
for _ in range(n):
    data = input().split()
    if data[0]=='push':
        stack.append(int(data[1]))
    elif data[0]=='pop':
        print(stack.pop() if stack else -1)
    elif data[0]=='size':
        print(len(stack))
    elif data[0]=='empty':
        print(0 if stack else 1)
    elif data[0]=='top':
        print(stack[-1] if stack else -1)