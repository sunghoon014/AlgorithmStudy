n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

stack = []
def dfs():
    if len(stack)==m:
        print(*stack)
        return
    for i in range(n):
        stack.append(data[i])
        dfs()
        stack.pop()
dfs()