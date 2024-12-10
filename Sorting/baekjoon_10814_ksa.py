import sys
N = int(sys.stdin.readline())
sorted_name = []
for _ in range(N):
    ages, names = sys.stdin.readline().strip().split(" ")
    sorted_name.append([int(ages), names])

for i in sorted(sorted_name, key=lambda x:x[0]):
    print(i[0], i[1])
