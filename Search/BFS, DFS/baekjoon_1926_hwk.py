# BFS
from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
drs = [0, 0, -1, 1]
dcs = [1, -1, 0, 0]
answer = 0
max_size = 0
for init_r in range(n):
    for init_c in range(m):
        if visited[init_r][init_c] or not grid[init_r][init_c]: continue 	# 방문했으면 건너뛰기
        answer += 1	# 그림 개수 추가
        que = deque([(init_r, init_c)])
        visited[init_r][init_c] = 1
        size = 0
        while que:
            r, c = que.popleft()
            size += 1
            for dr, dc in zip(drs, dcs):
                nr = r+dr
                nc = c+dc
                if 0<=nr<n and 0<=nc<m and grid[nr][nc] and not visited[nr][nc]:
                    que.append((nr, nc))
                    visited[nr][nc]=1
        max_size = max(max_size, size)

print(answer)
print(max_size)

# DFS