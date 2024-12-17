import sys
from collections import deque

N, K = map(int, input().split())

q = deque()
q.append(N)
visited = [0] * 100001
visited[N] = 1

if N == K:
    print("0")
    sys.exit()

while True:
    x = q.popleft()

    nx = x + 1
    if nx == K:
        print(visited[x])
        sys.exit()
    if nx <= 100000 and visited[nx] == 0:
        visited[nx] = visited[x] + 1
        q.append(nx)
    nx = x - 1
    if nx == K:
        print(visited[x])
        sys.exit()
    if nx >= 0 and visited[nx] == 0:
        visited[nx] = visited[x] + 1
        q.append(nx)
    nx = x * 2
    if nx == K:
        print(visited[x])
        sys.exit()
    if nx <= 100000 and visited[nx] == 0:
        visited[nx] = visited[x] + 1
        q.append(nx)