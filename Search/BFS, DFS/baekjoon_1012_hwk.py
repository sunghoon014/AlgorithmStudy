from collections import deque
T = int(input())
drs = [0, 0, 1, -1]
dcs = [1, -1, 0, 0]
for _ in range(T):
    M, N, K = map(int, input().split())
    vegs = [[0]*M for _ in range(N)]
    idxs = []
    for _ in range(K):
        j, i = map(int, input().split())
        vegs[i][j] = 1
        idxs.append((i, j))

    visited = [[0]*M for _ in range(N)]
    answer = 0
    for i, j in idxs:
        if visited[i][j]: continue
        que = deque([(i, j)])
        answer += 1
        while que:
            r, c = que.popleft()
            for idx in range(4):
                nr = r+drs[idx]
                nc = c+dcs[idx]
                if 0<=nr<N and 0<=nc<M and vegs[nr][nc] and not visited[nr][nc]:
                    que.append((nr, nc))
                    visited[nr][nc] = 1

    print(answer)
