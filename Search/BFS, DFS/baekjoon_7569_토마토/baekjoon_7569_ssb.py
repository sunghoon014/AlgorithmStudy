import sys
from collections import deque

input = sys.stdin.readline
m, n, h = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

start = []
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k]==1:
                start.append((i, j, k))

def bfs(start):
    queue = deque(start)
    max_day = 0
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0<=nx<h and 0<=ny<n and 0<=nz<m and box[nx][ny][nz]==0:
                box[nx][ny][nz]=box[x][y][z]+1
                queue.append((nx, ny, nz))
                max_day = max(max_day, box[nx][ny][nz])
    return max_day

max_days = bfs(start)-1

if any(box[i][j][k]==0 for i in range(h) for j in range(n) for k in range(m)):
    print(-1)
else:
    print(max(max_days, 0)) # 처음부터 모두 익은 상태 고려 (-> 답이 max_day=0인데, 위에서 -1함으로써 -1이 됨을 방지)