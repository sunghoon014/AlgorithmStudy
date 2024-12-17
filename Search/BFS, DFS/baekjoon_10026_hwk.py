from collections import deque

N = int(input())
pic = []
dis_pic = []
for _ in range(N):
    row = list(input())
    pic.append(row)
    dis_row = [chr if chr!="G" else "R" for chr in row]
    dis_pic.append(dis_row)

visited = [[0]*N for _ in range(N)]
dis_visited = [[0]*N for _ in range(N)]
drs = [0, 0, 1, -1]
dcs = [1, -1, 0, 0]

answer = 0
dis_answer = 0

# 적록색약 아님
for i in range(N):
    for j in range(N):
        if visited[i][j]: continue
        answer += 1
        que = deque([(i, j)])
        visited[i][j] = 1
        while que:
            r, c = que.popleft()
            for idx in range(4):
                nr = r + drs[idx]
                nc = c + dcs[idx]
                if 0<=nr<N and 0<=nc<N and pic[r][c]==pic[nr][nc] and not visited[nr][nc]:
                    que.append((nr, nc))
                    visited[nr][nc] = 1
# 적록색약
          
for i in range(N):
    for j in range(N):
        if dis_visited[i][j]: continue
        dis_answer += 1
        que = deque([(i, j)])
        dis_visited[i][j] = 1
        while que:
            r, c = que.popleft()
            for idx in range(4):
                nr = r + drs[idx]
                nc = c + dcs[idx]
                if 0<=nr<N and 0<=nc<N and dis_pic[r][c]==dis_pic[nr][nc] and not dis_visited[nr][nc]:
                    que.append((nr, nc))
                    dis_visited[nr][nc] = 1
print(answer, dis_answer)