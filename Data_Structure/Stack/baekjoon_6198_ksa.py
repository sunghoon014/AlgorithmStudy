import sys
N = int(sys.stdin.readline()) #빌딩의 개수
height = [int(sys.stdin.readline()) for _ in range(N)]
stack = []
sum = 0
for i in height:
    while stack and stack[-1] <= i:
        stack.pop()
    sum += len(stack)
    stack.append(i)
print(sum)