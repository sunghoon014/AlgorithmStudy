# 15651 N과M(3)
N,M=map(int,input().split())
stack=[]

def dfs():
    if len(stack)==M:
        print(*stack)
        return
    
    for i in range(1,N+1):
        stack.append(i)
        dfs()
        stack.pop()

dfs()
