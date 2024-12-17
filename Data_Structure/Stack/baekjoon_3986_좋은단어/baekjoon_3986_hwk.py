N = int(input())
answer = 0
for _ in range(N):
    string = list(input())
    stack = [string[0]]
    for s in string[1:]:
        if len(stack)!=0 and stack[-1]==s:
            stack.pop()
        else:
            stack.append(s)
    if not len(stack):
        answer += 1

print(answer)