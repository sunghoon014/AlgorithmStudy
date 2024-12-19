n, m = map(int, input().split())
stack = []

def dfs():
    if len(stack)==m:
        print(*stack)
        return
    for i in range(1, n+1):
        if stack:
            if stack[-1]>i:
                continue
        stack.append(i)
        dfs()
        stack.pop()

dfs()