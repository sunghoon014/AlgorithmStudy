# 15664 N과M(10)
N,M=map(int,input().split())
N_list=sorted(list(map(int,input().split())))
stack=[]

def dfs(start):
    check=0

    if len(stack)==M:
        print(*stack)
        return
    
    for idx in range(start,N):
        if check!=N_list[idx]:
            stack.append(N_list[idx])
            check=N_list[idx]
            dfs(idx+1)
            stack.pop()
dfs(0)
