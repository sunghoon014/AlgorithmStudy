import sys

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
answer = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == 0:
            cnt += 1
            stack = [(i, j)]
            visited[i][j] = cnt
            while stack:
                x, y = stack.pop()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1 and visited[nx][ny] == 0:
                        stack.append((nx, ny))
                        visited[nx][ny] = cnt
            answer.append(0)

# 각 영역 개수 세기
for i in range(N):
    for j in range(N):
        if visited[i][j] != 0:
            answer[visited[i][j] - 1] += 1
answer.sort()
print(cnt)
print("\n".join(map(str, answer)))
