# 3986 좋은 단어
N=int(input())
cnt=0
for _ in range(N):
    stack=[]
    string=input()
    for idx in range(len(string)):
        if len(stack)!=0 and stack[-1]==string[idx]:
            stack.pop()
        else:
            stack.append(string[idx])
    if len(stack)==0:
        cnt+=1
print(cnt)