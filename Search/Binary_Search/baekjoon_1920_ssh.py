import sys

input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
A = set(map(int, data[1].split()))
M = int(data[2])

number_to_find = list(map(int, data[3].split()))
for i in range(M):
    if number_to_find[i] in A:
        print("1")
    else:
        print("0")