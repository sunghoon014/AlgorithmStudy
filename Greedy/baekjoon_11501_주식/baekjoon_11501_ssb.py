t = int(input())
for _ in range(t):
    n = int(input())
    data = list(map(int, input().split()))
    max = 0
    money = 0
    for i in range(n-1, -1, -1):
        if data[i]>=max:
            max = data[i]
        else:
            money += max-data[i]
    print(money)