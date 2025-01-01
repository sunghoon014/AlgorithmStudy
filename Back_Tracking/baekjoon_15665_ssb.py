n, m = map(int, input().split())
data = sorted(set(map(int, input().split())))

stack = []
result = []
def dfs():
    if len(stack)==m:
        print(*stack)
        return
    for i in data:
        stack.append(i)
        dfs()
        stack.pop()

dfs()