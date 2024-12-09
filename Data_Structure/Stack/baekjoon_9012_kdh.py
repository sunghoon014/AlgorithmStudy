# 9012 괄호
N=int(input())
for _ in range(N):
    stack=[]
    already_NO=False
    string=input()
    for idx in range(len(string)):
        if string[idx]==')':
            if len(stack)!=0 and stack[-1]=='(':
                stack.pop()
            else:
                print("NO")
                already_NO=True
                break
        else:
            stack.append(string[idx])

    if already_NO:
        continue
    if len(stack)==0:
        print("YES")
    else:
        print("NO")