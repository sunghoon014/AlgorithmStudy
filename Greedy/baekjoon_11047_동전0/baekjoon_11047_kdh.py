# 11047 동전 0
N,K=map(int,input().split())
coin_list=[int(input()) for _ in range(N)]
result=0
for idx in range(N,-1,-1):
    if idx==N:
        continue
    if K//coin_list[idx]>=1:
        result+=K//coin_list[idx]
        K%=coin_list[idx]
print(result)