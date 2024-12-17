# 4949 균형잡힌 세상
while True:
    sentence=input().rstrip()
    stack=[]
    is_break=False
    if sentence=='.':
        exit()
    else:
        for char in sentence:
            if char=='(' or char=='[':
                stack.append(char)
            elif char==')':
                if len(stack)!=0 and stack[-1]=='(':
                    stack.pop()
                else:
                    print('no')
                    is_break=True
                    break
            elif char==']':
                if len(stack)!=0 and stack[-1]=='[':
                    stack.pop()
                else:
                    print('no')
                    is_break=True
                    break
            elif char=='.':
                break
        if len(stack)==0:
            if is_break==False:
                print('yes')
            else:
                continue
        else:
            if is_break==False:
                print('no')
            else:
                continue