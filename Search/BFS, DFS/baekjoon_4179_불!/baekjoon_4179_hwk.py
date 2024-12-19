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
        if grid[r][c]=="J" and (r==0 or r==N-1 or c==0 or c==M-1):    # 지훈이 가장자리에 도달하여 탈출
            return visited[r][c]
        for i in range(4):
            nr = r+drs[i]
            nc = c+dcs[i]
            if 0<=nr<N and 0<=nc<M and grid[nr][nc]=='.':
                if grid[r][c] == "J":   # 지훈이일 경우
                    grid[nr][nc] = "J"
                    visited[nr][nc] = visited[r][c]+1    # 이동한 시간 기록하면서 가기
                elif grid[r][c]=="F":   # 불일 경우
                    grid[nr][nc] = "F"
                que.append((nr, nc))    # 지훈이든 불이든 상관 없이 추가함. grid로 구별할거니까 여기서 구별할 필요 없음
    # 중간에 return 못하면 탈출 못한거니까 불가능 반환
    return "IMPOSSIBLE"

print(BFS(queue, visited))