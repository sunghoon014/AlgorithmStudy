import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    if x<0 or x>=m or y<0 or y>=n:
        return False
    if graph[x][y]==1:
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

t = int(input())
for _ in range(t):
    m, n ,k = map(int, input().split())
    graph = [[0]*n for _ in range(m)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1
    result = 0
    for i in range(m):
        for j in range(n):
            if dfs(i, j)==True:
                result += 1
    print(result)