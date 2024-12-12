import bisect

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

b.sort()
result = []
for i in range(n):
    temp = bisect.bisect(b, a[i])
    if b[temp-1] != a[i]:
        result.append(a[i])

result.sort()
print(len(result))
if result:
    result_str = list(map(str, result))
    print(' '.join(result_str))