stack = []
n = int(input())
for _ in range(n):
    command = input().split()
    if len(command)>1:
        com, num = command
        stack.append(int(num))
    else:
        command = command[0]
        if command=='pop':
            print(stack.pop() if len(stack) else -1)
        elif command=='size':
            print(len(stack))
        elif command=='empty':
            print(0 if len(stack) else 1)
        elif command=='top':
            print(stack[-1] if len(stack) else -1)
