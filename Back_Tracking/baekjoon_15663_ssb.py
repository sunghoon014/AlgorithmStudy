n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

stack = []
visited = [False]*n
result = []
def dfs():
    if len(stack)==m:
        tp = tuple(stack)
        result.append(tp)
        return
    for i in range(n):
        if visited[i]:
            continue
        stack.append(data[i])
        visited[i] = True
        dfs()
        visited[i] = False
        stack.pop()

dfs()
result = sorted(set(result))
for r in result:
    print(*r)