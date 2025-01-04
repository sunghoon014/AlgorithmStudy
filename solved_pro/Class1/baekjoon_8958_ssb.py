t = int(input())
for _ in range(t):
    data = list(input())
    result = []
    cnt = 0
    for d in data:
        if d=='O':
            cnt += 1
            result.append(cnt)
        else:
            cnt = 0
    print(sum(result))