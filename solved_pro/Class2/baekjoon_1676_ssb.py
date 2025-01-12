n = int(input())

fac = 1
for i in range(1, n+1):
    fac *= i

cnt = 0
for i in list(str(fac))[::-1]:
    if i=='0':
        cnt += 1
    else:
        break
print(cnt)