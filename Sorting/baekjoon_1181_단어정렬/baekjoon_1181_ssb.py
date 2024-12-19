n = int(input())
data = list(set(input() for _ in range(n)))
data.sort(key=lambda x: (len(x), x))

for word in data:
    print(word)