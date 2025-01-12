n = int(input())

cnt = []
for i in range(n//3+1):
    for j in range(n//5+1):
        if 3*i+5*j==n:
            cnt.append(i+j)

print(min(cnt) if cnt else -1)