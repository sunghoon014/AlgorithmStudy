import sys
x = list(sys.stdin.readline())
stick = 0
stack = []
pre = ''

for i in x:
    if i == '(':
        stack.append(i)
    elif i == ')':
        if pre == '(':
            stack.pop()
            stick += len(stack)
        else:
            stack.pop()
            stick += 1
    pre = i
            
print(stick)