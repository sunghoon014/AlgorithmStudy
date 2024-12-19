import sys

input = sys.stdin.readline

k, n = map(int, input().split())
l_lst = [int(input()) for _ in range(k)]
l_lst.sort()

start = 1
end = l_lst[0]

result = 0
while start <= end:
    mid = (start + end) // 2
    c = 0
    for l in l_lst:
        c += l // mid

    if c >= n:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
