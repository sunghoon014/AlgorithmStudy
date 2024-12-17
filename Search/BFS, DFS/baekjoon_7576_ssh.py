from collections import deque
import sys

def BFS (start_list):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque()
    for x, y in start_list:
        q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and tomato[nx][ny] == 0:
                q.append([nx, ny])
                tomato[nx][ny] = tomato[x][y] + 1

M, N = map(int, sys.stdin.readline().split())
tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

start_list = []
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            start_list.append([i, j])

BFS(start_list)

tomato_dimension = sum(tomato, [])

if 0 in tomato_dimension:
    print(-1)
else:
    print(max(tomato_dimension) - 1)