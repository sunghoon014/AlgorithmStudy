import sys
from collections import deque

def BFS(x, y, character):
    q = deque()
    q.append([x, y])
    picture_visited[x][y] = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and picture_visited[nx][ny] == 0 and picture[nx][ny] == character:
                picture_visited[nx][ny] = 1
                q.append([nx, ny])

N = int(sys.stdin.readline())
picture = [list(sys.stdin.readline().strip()) for _ in range(N)]
picture_visited = [[0] * len(row) for row in picture]

count = 0
for i in range(N):
    for j in range(N):
        if picture_visited[i][j] == 0:
            count += 1
            BFS(i, j, picture[i][j])

for i in range(N):
    for j in range(N):
        if picture[i][j] == 'G':
            picture[i][j] = 'R'
picture_visited = [[0] * len(row) for row in picture]

rg_count = 0
for i in range(N):
    for j in range(N):
        if picture_visited[i][j] == 0:
            rg_count += 1
            BFS(i, j, picture[i][j])

print(count, rg_count)