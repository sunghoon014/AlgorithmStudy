# 15650 N과 M (2)
N,M=map(int,input().split())
stack=[]

def dfs(start):
    
    if len(stack)==M:
        print(*stack)
        return
    
    for i in range(start,N+1):
        stack.append(i)
        dfs(i+1) # 이전 stack에 들어간 수보다 1 큰수가 들어가야한다. 4 4 의 결과는 1 2 3 4 한개 뿐이여야함
        stack.pop()

dfs(1)