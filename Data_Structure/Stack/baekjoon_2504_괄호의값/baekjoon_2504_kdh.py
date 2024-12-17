# 2504 괄호의 값
string=input()
stack=[]
for idx in range(len(string)):
    if string[idx]==')':
        if len(stack)!=0 and '(' in stack:
            if string[idx-1]=='(':
                stack.pop()
                stack.append(2)
            else:
                temp_score=0
                while stack:
                    popped=stack.pop()
                    if popped=='[':
                        print(0)
                        exit()
                    elif popped=='(':
                        stack.append(temp_score*2)
                        break
                    else:
                        temp_score+=popped
        else:
            print(0)
            exit()

    elif string[idx]==']':
        if len(stack)!=0 and '[' in stack:
            if string[idx-1]=='[':
                stack.pop()
                stack.append(3)
            else:
                temp_score=0
                while stack:
                    popped=stack.pop()
                    if popped=='(':
                        print(0)
                        exit()
                    elif popped=='[':
                        stack.append(temp_score*3)
                        break
                    else:
                        temp_score+=popped
        else:
            print(0)
            exit()
    

    else:
        stack.append(string[idx])

try:
    print(sum(stack))
except:
    print(0)