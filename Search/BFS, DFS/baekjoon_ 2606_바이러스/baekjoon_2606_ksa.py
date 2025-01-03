def dfs(graph, v, visited):
   visited[v] = True
   for i in graph[v]:
       if not visited[i]:
           dfs(graph, i, visited)

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
   a, b = map(int, input().split())
   graph[a].append(b)
   graph[b].append(a)

visited = [False] * (n+1)

dfs(graph, 1, visited)

print(sum(visited) - 1)