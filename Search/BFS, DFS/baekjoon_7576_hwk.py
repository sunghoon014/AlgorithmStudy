# BFS
from collections import deque

m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
drs = [0, 0, -1, 1]
dcs = [1, -1, 0, 0]

num_tomatos = 0
que = deque()
for i in range(n):
    for j in range(m):
        if grid[i][j]==0:
            num_tomatos+=1
        elif grid[i][j]>0:
            que.append((i, j))
            visited[i][j] = 1

answer = 1
while que:
    r, c = que.popleft()
    for dr, dc in zip(drs, dcs):
        nr = r+dr
        nc = c+dc
        if 0<=nr<n and 0<=nc<m and grid[nr][nc]==0 and not visited[nr][nc]:
            que.append((nr, nc))
            visited[nr][nc] = visited[r][c] + 1
            answer = max(answer, visited[nr][nc])
            num_tomatos -= 1

print(answer-1 if num_tomatos==0 else -1)

# DFS 로는 풀 수 없음
# 토마토가 익는 것은 근처에 있는 토마토들을 서서히 잠식해 나가는 방식이기 때문에
# 깊이 우선 탐색인 DFS를 사용할 수 없음