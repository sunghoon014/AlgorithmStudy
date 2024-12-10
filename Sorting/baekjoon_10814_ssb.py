n = int(input())

info = []
for _ in range(n):
    data = input()
    info.append(data)

info.sort(key=lambda x: int(x.split()[0]))

for people in info:
    print(people)