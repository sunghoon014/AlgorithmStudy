from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

queue = deque()
for _ in range(n):
    data = input().strip()
    if data == 'pop':
        print(queue.popleft() if queue else -1)
    elif data == 'size':
        print(len(queue))
    elif data == 'empty':
        print(0 if queue else 1)
    elif data == 'front':
        print(queue[0] if queue else -1)
    elif data == 'back':
        print(queue[-1] if queue else -1)
    else:
        _, value = data.split()
        queue.append(int(value))