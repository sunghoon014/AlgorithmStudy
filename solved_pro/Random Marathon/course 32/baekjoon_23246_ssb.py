n = int(input())

people = []
for _ in range(n):
    b, p, q, r = map(int, input().split())
    people.append((b, p*q*r, p+q+r))

people.sort(key=lambda x: (x[1], x[2], x[0]))
print(people[0][0], people[1][0], people[2][0])