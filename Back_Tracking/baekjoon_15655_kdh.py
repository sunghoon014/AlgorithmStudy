# 15655 N과 M(6)
N,M=map(int,input().split())
N_list=list(map(int,input().split()))
N_list.sort()
stack=[]

def dfs(start_idx):
    if len(stack)==M:
        print(*stack)
        return
    for idx in range(start_idx,len(N_list)):
        stack.append(N_list[idx])
        dfs(idx+1)
        stack.pop()

dfs(0)