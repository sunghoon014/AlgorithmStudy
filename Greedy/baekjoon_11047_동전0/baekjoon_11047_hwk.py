N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

answer = 0
while K!=0:
    coin = coins.pop()
    if K//coin==0:  # 현재 동전은 사용할 수 없음
        continue
    answer += K//coin
    K -= K//coin * coin

print(answer)
