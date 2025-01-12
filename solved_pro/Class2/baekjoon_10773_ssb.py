k = int(input())

stack = []
for _ in range(k):
    data = int(input())
    stack.append(data) if data else stack.pop()

print(sum(stack))