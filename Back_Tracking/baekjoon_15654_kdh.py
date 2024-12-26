# 15654 N과M (5)
N,M=map(int,input().split())
N_list=list(map(int,input().split()))
stack=[]
N_list.sort()
visited=[False]*(N_list[-1]+1)


def dfs():
    if len(stack)==M:
        print(*stack)
        return
    
    for num in N_list:
        if visited[num]:
            continue
        stack.append(num)
        visited[num]=True
        dfs()
        stack.pop()
        visited[num]=False

dfs()