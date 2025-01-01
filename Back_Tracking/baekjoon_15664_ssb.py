n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

stack = []
visited = [False]*n
result = []
def dfs():
    if len(stack)==m:
        result.append(tuple(stack))
        return
    for i in range(n):
        if visited[i]:
            continue
        if stack:
            if data[i]<stack[-1]:
                continue
        stack.append(data[i])
        visited[i] = True
        dfs()
        visited[i] = False
        stack.pop()

dfs()
for r in sorted(set(result)):
    print(*r)