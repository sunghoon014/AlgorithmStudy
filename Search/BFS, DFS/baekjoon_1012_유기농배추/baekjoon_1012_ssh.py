import sys
from collections import deque

T = int(sys.stdin.readline())

def BFS(x, y):
    field[x][y] += 1
    q = deque()
    q.append([x, y])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and field[nx][ny] == 1:
                field[nx][ny] += 1
                q.append([nx, ny])
            

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    field = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        field[y][x] = 1
    
    count = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                BFS(i, j)
                count += 1

    print(count)