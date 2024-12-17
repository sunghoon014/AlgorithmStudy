import sys
input = sys.stdin.readline

N = int(input())
heights = [int(input()) for _ in range(N)]
stack = []
cnt = 0

for i in heights:
    
    while stack and stack[0]<i:
        stack.pop()
        cnt += 1
    if stack:
        if stack[0] == i:
            if len(stack) == 1 or stack[1][0] <= i:
                cnt += stack[0][1]
            else:
                cnt += 1
        else:
            cnt += len(set(stack))
            if stack[-1] < i:
                stack.pop()

    stack.append(i)

print(cnt)


