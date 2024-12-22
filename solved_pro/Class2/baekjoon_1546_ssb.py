n = int(input())
data = list(map(int, input().split()))
data.sort()
m = data[-1]
mean = sum(map(lambda x: x/m*100, data))/n
print(mean)