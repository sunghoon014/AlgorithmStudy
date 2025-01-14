n = int(input())
people = []
for i in range(1, n+1):
    s, c, l = map(int, input().split())
    people.append((s, c, l, i))
people.sort(key=lambda x: (-x[0], x[1], x[2]))
print(people[0][3])