# BFS
from collections import deque

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
drs = [0, 0, -1, 1]
dcs = [1, -1, 0, 0]
num = 0
max_size = 0
for init_r in range(N):
    for init_c in range(M):
        if visited[init_r][init_c] or not grid[init_r][init_c]: continue 	# 방문했으면 건너뛰기
        num += 1	# 그림 개수 추가
        que = deque([(init_r, init_c)])
        visited[init_r][init_c] = 1
        size = 0
        while que:
            r, c = que.popleft()
            size += 1
            for dr, dc in zip(drs, dcs):
                nr = r+dr
                nc = c+dc
                if 0<=nr<N and 0<=nc<M and grid[nr][nc] and not visited[nr][nc]:
                    que.append((nr, nc))
                    visited[nr][nc]=1
        max_size = max(max_size, size)

print(num)
print(max_size)

# DFS
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
drs = [0, 0, -1, 1]
dcs = [1, -1, 0, 0]
stack = []
max_size = 0
num = 0
for i in range(N):
    for j in range(M):
        if grid[i][j]==0 or visited[i][j]: continue
        num += 1
        visited[i][j] = 1
        stack.append((i, j))
        size = 0
        while stack:
            r, c = stack.pop()
            size += 1
            for dr, dc in zip(drs, dcs):
                nr = r+dr
                nc = c+dc
                if 0<=nr<N and 0<=nc<M and grid[nr][nc] and not visited[nr][nc]:
                    stack.append((nr, nc))
                    visited[nr][nc] = 1
        max_size = max(max_size, size)
        
print(num)
print(max_size)