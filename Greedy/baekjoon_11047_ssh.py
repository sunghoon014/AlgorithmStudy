import sys

input = sys.stdin.read
data = input().splitlines()
N, K = map(int, data[0].split())

A = [ data[i] for i in range(1, N + 1) ]

total = 0
for coin in reversed(A):
    total += K // int(coin)
    K = K % int(coin)

print(total)