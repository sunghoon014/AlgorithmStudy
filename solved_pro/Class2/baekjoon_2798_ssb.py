n, m = map(int, input().split())
data = list(map(int, input().split()))

stack = []
visited = [False]*n
sum_card = 0
def dfs(start):
    global sum_card
    if len(stack)==3:
        new_sum = sum(stack)
        if m-new_sum>=0 and new_sum>sum_card:
            sum_card = new_sum
        return
    for i in range(start, n):
        if visited[i]:
            continue
        visited[i] = True
        stack.append(data[i])
        dfs(i+1)
        stack.pop()
        visited[i] = False

dfs(0)
print(sum_card)