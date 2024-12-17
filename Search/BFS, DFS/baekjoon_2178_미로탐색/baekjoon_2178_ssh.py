from collections import deque

def BFS(x, y):
    q = deque()
    q.append([x, y])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while True:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1:
                q.append([nx, ny])
                maze[nx][ny] = maze[x][y] + 1
            
            if nx == N - 1 and ny == M - 1:
                return


N, M = map(int, input().split())

maze = [list(map(int, list(input()))) for _ in range(N)]

BFS(0, 0)
print(maze[N - 1][M - 1])
