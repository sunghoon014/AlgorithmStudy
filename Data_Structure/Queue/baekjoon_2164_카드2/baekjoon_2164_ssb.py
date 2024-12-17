from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
queue = deque()
queue.extend(range(1, n+1))

while len(queue)>1:
    queue.popleft()
    temp = queue.popleft()
    queue.append(temp)

print(queue.pop())