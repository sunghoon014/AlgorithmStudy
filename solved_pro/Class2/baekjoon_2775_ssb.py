t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    lst = [i for i in range(1, n+1)]
    for _ in range(1, k+1):
        lst = [sum(lst[:i]) for i in range(1, n+1)]
    print(lst[-1])