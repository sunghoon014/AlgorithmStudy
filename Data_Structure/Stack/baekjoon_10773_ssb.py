n = int(input())

stack = []
for _ in range(n):
    data = int(input())
    if data != 0:
        stack.append(data)
    else:
        stack.pop()

print(sum(stack))