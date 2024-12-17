import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
grid = [input().strip() for _ in range(N)]
M = len(grid[0])

visited1 = [[0] * M for _ in range(N)]
visited2 = [[0] * M for _ in range(N)]
dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]
n1 = 0
n2 = 0
for x in range(M):
    for y in range(N):
        # 색맹이 아닌 경우
        if not visited1[y][x]:
            n1 += 1
            que1 = deque([(x, y)])
            visited1[y][x] = 1
            while que1:
                que_x, que_y = que1.popleft()
                i = grid[y][x]
                for dx, dy in zip(dxs, dys):
                    nx = que_x + dx
                    ny = que_y + dy
                    if 0 <= nx < M and 0 <= ny < N and grid[ny][nx] == i and not visited1[ny][nx]:
                        que1.append((nx, ny))
                        visited1[ny][nx] = 1

        # 색맹인 경우
        if not visited2[y][x]:
            n2 += 1
            que2 = deque([(x, y)])
            visited2[y][x] = 1
            while que2:
                que_x, que_y = que2.popleft()
                i = grid[y][x]
                if i == "B":
                    for dx, dy in zip(dxs, dys):
                        nx = que_x + dx
                        ny = que_y + dy
                        if 0 <= nx < M and 0 <= ny < N and grid[ny][nx] == i and not visited2[ny][nx]:
                            que2.append((nx, ny))
                            visited2[ny][nx] = 1
                else:
                    for dx, dy in zip(dxs, dys):
                        nx = que_x + dx
                        ny = que_y + dy
                        if 0 <= nx < M and 0 <= ny < N and grid[ny][nx] != "B" and not visited2[ny][nx]:
                            que2.append((nx, ny))
                            visited2[ny][nx] = 1

print(n1, n2)
