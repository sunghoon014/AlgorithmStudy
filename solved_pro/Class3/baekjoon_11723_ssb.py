import sys
input = sys.stdin.readline
n = int(input())

s = []
for _ in range(n):
    data = list(input().strip().split())
    if data[0]=='add':
        s.append(int(data[1]))
        s = list(set(s))
    elif data[0]=='remove':
        if int(data[1]) in s:
            s.remove(int(data[1]))
    elif data[0]=='check':
        if int(data[1]) in s:
            print(1)
        else:
            print(0)
    elif data[0]=='toggle':
        if int(data[1]) in s:
            s.remove(int(data[1]))
        else:
            s.append(int(data[1]))
    elif data[0]=='all':
        s = [i+1 for i in range(20)]
    elif data[0]=='empty':
        s = []