n = int(input()) #컴퓨터의 수
m = int(input()) #네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가

graph = [[] for _ in range(n+1)] # [][2, 5][1, 3, 5][2][7][1, 2, 6][5][4]

for _ in range(m):
   a, b = map(int, input().split()) #1 2
   graph[a].append(b)
   graph[b].append(a)

visited = [0] * (n+1)


def dfs(graph, v, visited):
   visited[v] = True
   for i in graph[v]:
       if not visited[i]:
           dfs(graph, i, visited)

dfs(graph, 1, visited)

print(sum(visited) - 1)