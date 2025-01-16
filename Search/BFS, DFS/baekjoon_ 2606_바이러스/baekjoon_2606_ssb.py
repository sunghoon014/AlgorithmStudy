import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
t = int(input())

graph = defaultdict(list)
for _ in range(t):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

def dfs(graph, start):
    need_visit, visited = [], []
    need_visit.append(start)
    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited

virus = dfs(graph, 1)
print(len(virus)-1)