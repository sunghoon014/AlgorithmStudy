import sys

T = int(sys.stdin.readline())

for i in range(0, T):
    N = int(sys.stdin.readline())
    days = list(map(int, sys.stdin.readline().split()))
    profit, max_price = 0, 0
    for j in range(len(days)-1, -1, -1):
        if days[j] > max_price:
            max_price = days[j]
        else:
            profit += max_price - days[j]
    
    print(profit)
