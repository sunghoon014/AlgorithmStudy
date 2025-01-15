import sys

input = sys.stdin.readline
n, m = map(int, input().split())

dict = {}
for i in range(n):
    dict[i+1] = input().strip()

reverse_dict = {v: k for k, v in dict.items()}
for _ in range(m):
    data = input().strip()
    if data.isalpha():
        print(reverse_dict[data])
    elif data.isdigit():
        print(dict[int(data)])