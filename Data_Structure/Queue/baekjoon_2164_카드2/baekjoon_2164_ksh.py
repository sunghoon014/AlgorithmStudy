from collections import deque
import sys

input = sys.stdin.readline
n = int(input())

queue = deque([x + 1 for x in range(n)])
while True:
    if len(queue) == 1:
        print(queue[0])
        break
    queue.popleft()
    q = queue.popleft()
    queue.append(q)
