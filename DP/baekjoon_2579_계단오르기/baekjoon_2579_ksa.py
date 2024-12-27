n = int(input())
stair = [0] * (n+1)
dp = [0] * (n+1)

for i in range(n):
    stair[i] = int(input())

if n == 1:
    print(stair[0])
elif n == 2:
    print(max(stair[0] + stair[1], stair[1]))
else:
    dp[0] = stair[0]
    dp[1] = max(stair[0] + stair[1], stair[1])
    dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])

    for i in range(3, n):
        dp[i] = max(dp[i-3] + stair[i-1] + stair[i], 
                    dp[i-2] + stair[i])

    print(dp[n-1])