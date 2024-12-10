T = int(input())

for _ in range(T):
    N = int(input())
    prices = list(map(int, input().split())) #3 5 9 7 6
    
    max_profit = 0
    max_price = 0

    for price in reversed(prices):
        if price > max_price:
            max_price = price
        else:
            max_profit += max_price - price
            
    print(max_profit)

# T = int(input())

# for _ in range(T):
#     N = int(input())
#     prices = list(map(int, input().split()))
#     #3 5 9
#     buy = [] #3 5
#     output = 0
    
#     for i in range(N):
#         current = prices[i]
#         if i == N-1 or current > prices[i+1]:
#             if buy:
#                 for money in buy:
#                     output += current - money
#                 buy = []
#         elif current <= prices[i+1]:
#             buy.append(current)
#     print(output)

