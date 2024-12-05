from collections import deque
import sys

input = sys.stdin.readline
n = int(input())

queue = deque([])
for _ in range(n):
    instance = input().strip().split()
    if instance[0] == "push":
        queue.append(int(instance[1]))
    elif instance[0] == "pop":
        if len(queue) > 0:
            print(queue.popleft())
        else:
            print(-1)
    elif instance[0] == "size":
        print(len(queue))
    elif instance[0] == "empty":
        if len(queue) > 0:
            print(0)
        else:
            print(1)
    elif instance[0] == "front":
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)
    elif instance[0] == "back":
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)
