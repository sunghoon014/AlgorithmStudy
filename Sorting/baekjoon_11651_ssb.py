n = int(input())

data = [input() for _ in range(n)]
data.sort(key=lambda x: (int(x.split()[1]), int(x.split()[0])))

for point in data:
    print(point)