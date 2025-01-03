import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    if N == 0:
        print(1, 0)
        continue
    if N == 1:
        print(0, 1)
        continue

    d = [0] * (N + 1)
    d[0] = 1
    d[1] = 1

    for i in range(2, N + 1):
        d[i] = d[i - 1] + d[i - 2]
    print(d)
    print(d[N - 2], d[N - 1])


"""
for _ in range(T):
    N = int(input())
    if N == 0:
        print(1, 0)
        continue
    if N == 1:
        print(0, 1)
        continue

    d = [0] * (N + 1)

    def fibo(x):
        if x == 0 or x == 1:
            d[x] += 1
            return 1
        if d[x] != 0:
            d[x] += 1
        d[x] = fibo(x - 1) + fibo(x - 2)
        return 1

    fibo(N)
    print(d[0], d[1])
"""
