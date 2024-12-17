import sys
from collections import deque

inpurt = sys.stdin.readline
N, K = map(int, input().split())
visited = [0] * 100000
dxs = [1, -1, 2]

que = deque([N])
while que:
    x = que.popleft()
    if x == K:
        break

    for dx in dxs:
        if dx == 2:
            nx = x * dx
        else:
            nx = x + dx
        if 0 <= nx <= 100000 and not visited[nx]:
            que.append(nx)
            visited[nx] += 1

print(max(visited))
