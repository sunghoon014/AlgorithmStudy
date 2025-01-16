from collections import deque

n, k = map(int, input().split())

def bfs(start):
    queue = deque()
    queue.append(start)
    visited = [-1]*100001
    visited[start] = 0
    while queue:
        x = queue.popleft()
        if x==k:
            return visited[x]
        for i in [x-1, x+1, 2*x]:
            if 0<=i<=100000 and visited[i]==-1:
                visited[i] = visited[x]+1
                queue.append(i)

print(bfs(n))