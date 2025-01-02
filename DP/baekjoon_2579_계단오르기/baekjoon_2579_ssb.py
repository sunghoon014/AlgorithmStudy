n = int(input())
data = [int(input()) for _ in range(n)]

# 첫번째 계단: 1
# 두번째 계단: max(1>2, 2)
# 세번째 계단: max(1>3, 2>3(바로 전 계단에서 왔으면 전 계단은 전전 계단을 밟지 않음))
# 네번째 계단: max(max(2)>4) / 1>3>4
# 다섯번째 계단: max(max(3)>5, max(2)>4>5)

d = [0]*(n+1)
for i in range(1, n+1):
    if i==1:
        d[1] = data[0]
        continue
    if i==2:
        d[2] = max(data[0]+data[1], data[1])
        continue
    if i==3:
        d[3] = max(data[0]+data[2], data[1]+data[2])
        continue
    d[i] = max(d[i-2]+data[i-1], d[i-3]+data[i-2]+data[i-1])

print(d[n])