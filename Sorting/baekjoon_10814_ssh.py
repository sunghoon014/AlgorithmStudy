import sys

input = sys.stdin.read
data = input().splitlines()
N = int(data[0])

name_list = []
for i in range(1, N + 1):
    age = int(data[i].split()[0])
    name = data[i].split()[1]
    name_list.append([age, name])

name_list.sort(key=lambda x: x[0])

for age, name in name_list:
    print(age, name)