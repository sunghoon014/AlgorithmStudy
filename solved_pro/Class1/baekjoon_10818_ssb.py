# 324ms
n = int(input())
data = list(map(int, input().split()))
result = [min(data), max(data)]
print(*result)


# 636ms
# n = int(input())
# data = list(map(int, input().split()))
# data.sort()
# result = [data[0], data[-1]]
# print(*result)