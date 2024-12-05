# 10845 큐
import sys
from collections import deque
input=sys.stdin.readline
queue=deque()
N=int(input())
for _ in range(N):
    command=input().strip()
    if len(command.split())==2:
        queue.append(command.split()[1])
    else:
        if command=='pop':
            if len(queue)==0:
                print(-1)
            else:
                print(queue.popleft())
        elif command=='size':
            print(len(queue))
        elif command=='empty':
            if len(queue)==0:
                print(1)
            else:
                print(0)
        elif command=='front':
            if len(queue)==0:
                print(-1)
            else:
                print(queue[0])
        elif command=='back':
            if len(queue)==0:
                print(-1)
            else:
                print(queue[-1])
