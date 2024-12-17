from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort()
result = []
for num in b:
    try:
        if a[bisect_left(a, num)]==num:
            result.append('1')
        else:
            result.append('0')
    except IndexError:
        result.append('0')

print(' '.join(result))