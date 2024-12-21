n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

stack = []
def dfs():
    if len(stack)==m:
        print(*stack)
        return
    for i in range(n):
        if stack:
            if stack[-1]>data[i]:
                continue
        stack.append(data[i])
        dfs()
        stack.pop()
dfs()