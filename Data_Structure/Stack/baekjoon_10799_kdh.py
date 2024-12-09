# 10799 쇠막대기
string=input()
stack=[] 
laser=0
result=0
for idx in range(len(string)):
    if string[idx]==')':
        if string[idx-1]=='(':
            stack.pop()
            result+=len(stack)
        else:
            stack.pop()
            result+=1
    else:
        stack.append(string[idx])

print(result)