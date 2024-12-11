import bisect

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort()
for i in range(m):
    temp = bisect.bisect_left(a, b[i])
    try:
        if a[temp]==b[i]:
            print(1)
        else:
            print(0)
    except IndexError:
        print(0)