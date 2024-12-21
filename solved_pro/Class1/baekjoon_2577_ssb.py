from collections import defaultdict

a = int(input())
b = int(input())
c = int(input())
data = list(str(a*b*c))

dict = defaultdict(int)
for i in data:
    dict[int(i)] += 1

for j in range(10):
    print(dict[j])