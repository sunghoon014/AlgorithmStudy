import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

for _ in range(N):
    I = int(input())
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))

    visited = [[0] * I for _ in range(I)]
    # fmt: off
    dxs = [1+1,  1,    1+1,   1,    -1-1,  -1,    -1-1,  -1]
    dys = [1,    1+1, -1,    -1-1,  -1,    -1-1,   1,     1+1]
    # fmt: on

    que = deque([start])
    while que:
        x, y = que.popleft()
        if (x, y) == end:
            break

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < I and 0 <= ny < I and not visited[nx][ny]:
                que.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

    print(visited[end[0]][end[1]])
