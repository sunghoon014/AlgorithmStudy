import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
queue = deque()
visited = [[[0] * M for _ in range(N)] for _ in range(H)]

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

for z in range(H):
    for y in range(N):
        for x in range(M):
            if box[z][y][x] == 1:
                queue.append((z, y, x))
                visited[z][y][x] = 1

while queue:
    z, y, x = queue.popleft()
    for i in range(6):
        nz = z + dz[i]
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M and not visited[nz][ny][nx] and box[nz][ny][nx] == 0:
            visited[nz][ny][nx] = visited[z][y][x] + 1
            queue.append((nz, ny, nx))

result = 0
for z in range(H):
    for y in range(N):
        for x in range(M):
            if box[z][y][x] == 0 and visited[z][y][x] == 0:
                print(-1)
                exit()
            result = max(result, visited[z][y][x])

print(result - 1)
