import sys

input = sys.stdin.readline

n = int(input())
stack_origin = list(map(int, input().strip().split()))
stack_origin = stack_origin[::-1]
stack = stack_origin.copy()

result = []
for s in stack:
    if not stack:
        print(0)

    candi = 0
    for i, x in enumerate(stack_origin):
        idx = abs(i - len(stack_origin)) - 1
        if s >= x:
            candi = idx
            break
    stack.pop(0)

    print(s, candi, stack_origin, stack)
