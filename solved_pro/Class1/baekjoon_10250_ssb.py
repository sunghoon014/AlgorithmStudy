t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    yy = str(n%h if n%h else h)
    xx = str((n-1)//h + 1)
    if len(xx)==1:
        xx = '0'+xx
    print(yy+xx)