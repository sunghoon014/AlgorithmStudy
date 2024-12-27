import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = sorted(list(set(map(int, input().split()))))
N = len(numbers)
stack = []
visited = [0] * N

def DFS():
    if len(stack) == M:
        print(*stack)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            stack.append(numbers[i])
            DFS()
            stack.pop()
            visited[i] = 0
DFS()