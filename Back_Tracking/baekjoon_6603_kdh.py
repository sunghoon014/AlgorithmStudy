# 6603 로또
def dfs(start):
    if len(stack)==6:
        print(*stack)
        return
    
    for idx in range(start,k):
        stack.append(S[idx])
        dfs(idx+1)
        stack.pop()

while True:
    numbers=list(map(int,input().split()))
    if len(numbers)==1 and numbers[0]==0:
        exit()

    k=numbers[0]
    S=numbers[1:] # 오름차순으로 주어짐

    stack=[]
    dfs(0)
    print()