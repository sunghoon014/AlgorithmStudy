# 15666 N과M(12)
N,M=map(int,input().split())
N_list=sorted(list(map(int,input().split())))
stack=[]

def dfs(start):
    if len(stack)==M:
        print(*stack)
        return
    
    check=0
    for idx in range(start,N):
        if check!=N_list[idx]:
            check=N_list[idx]
            stack.append(N_list[idx])
            dfs(idx)
            stack.pop()

dfs(0)