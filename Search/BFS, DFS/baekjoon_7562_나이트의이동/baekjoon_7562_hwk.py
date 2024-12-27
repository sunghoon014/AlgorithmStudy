from collections import deque
T = int(input())
drs = [-2, -2, -1, 1, 2, 2, 1, -1]
dcs = [-1, 1, 2, 2, 1, -1, -2, -2]
for _ in range(T):
    I = int(input())
    R, C = map(int, input().split())
    queue = deque([(R, C)])
    to_r, to_c = map(int, input().split())
    visited = [[0]*I for _ in range(I)]
    visited[R][C] = 1
    while queue:
        r, c = queue.popleft()
        if r==to_r and c==to_c:
            break
        for i in range(8):
            nr = r + drs[i]
            nc = c + dcs[i]
            if 0<=nr<I and 0<=nc<I and not visited[nr][nc]:
                visited[nr][nc] = visited[r][c] + 1
                queue.append((nr, nc))

    print(visited[to_r][to_c]-1)