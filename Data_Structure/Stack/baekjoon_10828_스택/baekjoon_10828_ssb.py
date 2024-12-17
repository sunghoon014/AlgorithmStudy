n = int(input())

stack = []
for _ in range(n):
    data = input()
    if data == 'top':
        print(stack[-1] if stack else -1)
    elif data == 'size':
        print(len(stack))
    elif data == 'empty':
        print(0 if stack else 1)
    elif data == 'pop':
        print(stack.pop() if stack else -1)
    else:
        _, value = data.split()
        stack.append(int(value))