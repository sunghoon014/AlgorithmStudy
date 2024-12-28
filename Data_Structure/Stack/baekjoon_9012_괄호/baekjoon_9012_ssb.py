n = int(input())
for _ in range(n):
    stack = []
    data = list(input())
    for i in data:
        if i=='(':
            stack.append(i)
        else:
            try:
                stack.pop()
            except IndexError:
                stack.append(i)
                break
    if stack:
        print('NO')
    else:
        print('YES')