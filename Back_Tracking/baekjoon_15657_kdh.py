# 15657 N과M (8)
N,M=map(int,input().split())
N_list=list(map(int,input().split()))
N_list.sort()
stack=[]

def dfs(start):
    if len(stack)==M:
        print(*stack)
        return
    for idx in range(start,len(N_list)):
        stack.append(N_list[idx])
        dfs(idx)
        stack.pop()

dfs(0)