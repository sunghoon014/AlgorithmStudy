from collections import deque

n, k = map(int, input().split())
queue = deque([i+1 for i in range(n)])
result = []
while queue:
    for i in range(k):
        if i<k-1:
            queue.append(queue.popleft())
        elif i==k-1:
            result.append(queue.popleft())

result = ', '.join(list(map(str, result)))
print('<'+result+'>')