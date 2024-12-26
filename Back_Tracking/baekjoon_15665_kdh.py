# 15665 N과M (11)
N,M=map(int,input().split())
N_list=sorted(list(map(int,input().split())))
stack=[]

def dfs():
    if len(stack)==M:
        print(*stack)
        return
    
    check=0
    for idx in range(N):
        if check!=N_list[idx]:
            check=N_list[idx]
            stack.append(N_list[idx])
            dfs()
            stack.pop()

dfs()