import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    grid = [[0] * M for _ in range(N)]
    for _ in range(K):
        init_x, init_y = map(int, input().split())
        grid[init_y][init_x] = 1

    visited = [[0] * M for _ in range(N)]
    dxs = [1, -1, 0, 0]
    dys = [0, 0, 1, -1]
    num = 0
    for x in range(M):
        for y in range(N):
            if visited[y][x] or not grid[y][x]:
                continue

            num += 1
            que = deque([(x, y)])
            visited[y][x] = 1
            while que:
                que_x, que_y = que.popleft()
                for dx, dy in zip(dxs, dys):
                    nx = que_x + dx
                    ny = que_y + dy
                    if 0 <= nx < M and 0 <= ny < N and grid[ny][nx] and not visited[ny][nx]:
                        que.append((nx, ny))
                        visited[ny][nx] = 1
    print(num)
