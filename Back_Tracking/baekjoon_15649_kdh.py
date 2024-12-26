# 15649 N과 M
N,M=map(int,input().split())
stack=[]
visited=[False]*(N+1)

def dfs():
    
    if len(stack)==M:
        print(*stack)
        return
    
    for i in range(1,N+1):
        if visited[i]:
            continue
        stack.append(i)
        visited[i]=True
        dfs() # 무조건 오름차순일 필요는 없기에 중복되는 수만 골라지지않게 dfs로 호출한다. 4 4의 경우 1 2 3 4, 1 2 4 3, 1 3 2 4 등 다양한 답이 존재함
        visited[i]=False
        stack.pop()

dfs()