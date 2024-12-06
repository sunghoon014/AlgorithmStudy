# 6198 옥상 정원 꾸미기
import sys
input=sys.stdin.readline
N=int(input())
stack=[]
cnt=0 # append하면서 현재 stack size만큼 count
for _ in range(N):
    curr_height=int(input().strip())
    while stack:
        if stack[-1]>curr_height:
            cnt+=len(stack)
            break
        else:
            stack.pop()

    stack.append(curr_height)
    # print('stack_stat',stack)
    # print('cnt',cnt)

print(cnt)