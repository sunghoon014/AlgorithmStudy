# 17298 오큰수
N=int(input())
numbers=list(map(int,input().split()))
result=[-1]*N
stack=[]
for idx in range(N):
    while stack:
        if stack[-1][1]<numbers[idx]:
            popped_idx,popped_val=stack.pop()
            result[popped_idx]=numbers[idx]
        else:
            break
    stack.append((idx,numbers[idx]))
print(*result)