from collections import deque

n = int(input())

queue = deque()
for _ in range(n):
    data = input().split()
    if data[0] == 'push':
        queue.append(int(data[1]))
    elif data[0] == 'pop':
        print(queue.popleft() if queue else -1)
    elif data[0] == 'size':
        print(len(queue))
    elif data[0] == 'empty':
        print(0 if queue else 1)
    elif data[0] == 'front':
        print(queue[0] if queue else -1)
    elif data[0] == 'back':
        print(queue[-1] if queue else -1)