from collections import deque

queue = deque([])
n = int(input())
for _ in range(n):
    command = input().split()
    if len(command)>1:
        com, num = command
        queue.append(int(num))
    else:
        command = command[0]
        if command=='pop':
            print(queue.popleft() if len(queue) else -1)
        elif command=='size':
            print(len(queue))
        elif command=='empty':
            print(0 if len(queue) else 1)
        elif command=='front':
            print(queue[0] if len(queue) else -1)
        elif command=='back':
            print(queue[-1] if len(queue) else -1)