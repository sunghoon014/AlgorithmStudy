# BFS
from collections import deque

n, m = map(int, input().split())
grid = [input() for _ in range(n)]
visited = [[0]*m for _ in range(n)]
drs = [0, 0, -1, 1]
dcs = [1, -1, 0, 0]

visited[0][0] = 1
que = deque([(0, 0)])
while que:
    r, c = que.popleft()
    for dr, dc in zip(drs, dcs):
        nr = r+dr
        nc = c+dc
        if 0<=nr<n and 0<=nc<m and grid[nr][nc]=='1' and not visited[nr][nc]:
            que.append((nr, nc))
            visited[nr][nc] = visited[r][c] + 1

print(visited[n-1][m-1])

# DFS
