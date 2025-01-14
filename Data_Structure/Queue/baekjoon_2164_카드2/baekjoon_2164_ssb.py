# from collections import deque
# import sys
# input = sys.stdin.readline

# n = int(input())
# queue = deque()
# queue.extend(range(1, n+1))

# while len(queue)>1:
#     queue.popleft()
#     temp = queue.popleft()
#     queue.append(temp)

# print(queue.pop())

from collections import deque

n = int(input())
queue = deque(i+1 for i in range(n))
while len(queue)>1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue.popleft())