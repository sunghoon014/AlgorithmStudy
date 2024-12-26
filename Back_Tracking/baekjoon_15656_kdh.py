# 15656 N과 M(7)
N,M=map(int,input().split())
N_list=list(map(int,input().split()))
stack=[]
N_list.sort()
def dfs():
    if len(stack)==M:
        print(*stack)
        return
    
    for num in N_list:
        stack.append(num)
        dfs()
        stack.pop()

dfs()