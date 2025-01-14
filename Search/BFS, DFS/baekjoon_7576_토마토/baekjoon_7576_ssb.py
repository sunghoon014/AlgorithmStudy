import sys
from collections import deque

input = sys.stdin.readline
m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]

start = []
for i in range(n):
    for j in range(m):
        if tomato[i][j]==1:
            start.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start):
    queue = deque()
    for x, y in start:
        queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and tomato[nx][ny]==0:
                tomato[nx][ny] = tomato[x][y] + 1
                queue.append((nx, ny))

bfs(start)

tomato = sum(tomato, [])
if 0 in tomato:
    print(-1)
else:
    print(max(tomato)-1)