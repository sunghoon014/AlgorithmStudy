n = int(input())
data = [input() for _ in range(n)]
data.sort(key=lambda x: (-int(x.split()[1]), int(x.split()[2]), -int(x.split()[3]), x.split()[0]))
for x in data:
    print(x.split()[0])