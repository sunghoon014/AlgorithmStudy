from collections import deque

N, M = map(int, input().split())
grid = []
queue = deque([])
fire_init = []
for i in range(N):
    row = list(input())
    grid.append(row)
    if 'J' in row:
        J_init = (i, row.index('J'))
    if 'F' in row:
        fire_init.append((i, row.index('F')))

queue.extend(fire_init)
queue.append(J_init)
visited = [[0]*M for _ in range(N)]

visited[J_init[0]][J_init[1]]=1
drs = [0, 0, 1, -1]
dcs = [1, -1, 0, 0]
# #:벽, .:공간, J:지훈이 초기 위치, F:불

def BFS(que, visited):
    while que:
        r, c = que.popleft()
        for i in range(4):
            nr = r+drs[i]
            nc = c+dcs[i]
            if 0<=nr<N and 0<=nc<M and grid[nr][nc]=='.':
                if grid[r][c] == "J":   # 지훈이일 경우
                    grid[nr][nc] = "J"
                    visited[nr][nc] = visited[r][c]+1
                    if nr==0 or nr==N-1 or nc==0 or nc==M-1:    # 탈출
                        return visited[nr][nc]
                elif grid[r][c]=="F":   # 불일 경우
                    grid[nr][nc] = "F"
                que.append((nr, nc))

    return "IMPOSSIBLE"

if J_init[0]==0 or J_init[0]==N-1 or J_init[1]==0 or J_init[1]==M-1:
    print(1)
else:
    print(BFS(queue, visited))