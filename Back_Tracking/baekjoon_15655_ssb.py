n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

stack = []
visited = [False]*n
def dfs():
    if len(stack)==m:
        print(*stack)
    for i in range(n):
        if visited[i]:
            continue
        if stack:
            if stack[-1]>data[i]:
                continue
        stack.append(data[i])
        visited[i] = True
        dfs()
        visited[i] = False
        stack.pop()
dfs()