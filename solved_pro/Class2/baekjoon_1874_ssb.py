n = int(input())
data = [int(input()) for _ in range(n)]

i = 1
stack, result = [], []
for d in data:
    while d>=i:
        stack.append(i)
        result.append('+')
        i += 1
    if stack and d==stack[-1]:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        exit()

for r in result:
    print(r)