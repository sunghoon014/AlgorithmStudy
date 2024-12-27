# 15663 N과M(9)
N,M=map(int,input().split())
N_list=list(map(int,input().split()))
N_list.sort()
stack=[]
visited=[False]*N
def dfs():
    check=0
    if len(stack)==M:
        print(*stack)
        return
    
    for idx,num in enumerate(N_list): # 1 7 9 9
        if check!=num and not visited[idx]:
            stack.append(num)
            check=num
            visited[idx]=True
            dfs()
            stack.pop()
            visited[idx]=False



dfs()