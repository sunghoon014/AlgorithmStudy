n, m = map(int, input().split())
stack = []
visited = [False] * (n+1)
def dfs():
    if len(stack)==m:
        print(*stack)
        return
    for i in range(1, n+1):
        if visited[i]:
            continue
        stack.append(i)
        visited[i]=True
        dfs()
        visited[i]=False
        stack.pop()

dfs()