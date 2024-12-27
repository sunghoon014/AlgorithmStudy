def bt(n):
    if len(lot)==6:
        print(*lot)
        return
    for i in range(n, k):
        lot.append(S[i])
        bt(i+1)
        lot.pop()

while True:
    inp = list(map(int, input().split()))
    k = inp[0]
    if not k: break
    S = sorted(inp[1:])
    lot = []
    bt(0)
    print()