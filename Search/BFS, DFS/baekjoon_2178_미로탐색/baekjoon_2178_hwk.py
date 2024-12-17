# BFS
from collections import deque

N, M = map(int, input().split())
grid = [input() for _ in range(N)]
visited = [[0]*M for _ in range(N)]
drs = [0, 0, -1, 1]
dcs = [1, -1, 0, 0]

visited[0][0] = 1
que = deque([(0, 0)])
while que:
    r, c = que.popleft()
    for dr, dc in zip(drs, dcs):
        nr = r+dr
        nc = c+dc
        if 0<=nr<N and 0<=nc<M and grid[nr][nc]=='1' and not visited[nr][nc]:
            que.append((nr, nc))
            visited[nr][nc] = visited[r][c] + 1

print(visited[N-1][M-1])

# DFS 로는 풀 수 없음
# dfs를 하다보면 빙 돌아가는 경우가 있을 수 있는데, 그 경우에도 방문처리가 되기 때문에
# 최단 경로를 찾더라도 방문 처리 때문에 진행할 수가 없음
# not visited[nr][nc] or visited[nr][nc]>=visited[r][c]+1
# 이런 코드로 이미 방문한 곳이라도 지금 경로가 최단 경로인 것 같으면 탐색한다고 해도
# 시간 초과 발생