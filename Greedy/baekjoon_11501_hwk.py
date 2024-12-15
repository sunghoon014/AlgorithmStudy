T = int(input())
for _ in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    max_value = 0
    answer = 0
    while prices:
        price = prices.pop()
        if price > max_value:
            max_value = price
        answer += max_value-price
    print(answer)