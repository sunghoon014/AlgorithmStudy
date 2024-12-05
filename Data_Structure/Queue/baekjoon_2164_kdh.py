# 2164 카드2
from collections import deque
N=int(input())
queue=deque()
queue.extend(range(1,N+1))
while len(queue)>1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])