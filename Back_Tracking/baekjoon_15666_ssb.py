n, m = map(int, input().split())
data = sorted(set(map(int, input().split())))

stack = []
def dfs():
    if len(stack)==m:
        print(*stack)
        return
    for i in data:
        if stack:
            if i<stack[-1]:
                continue
        stack.append(i)
        dfs()
        stack.pop()

dfs()