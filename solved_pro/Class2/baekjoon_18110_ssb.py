import sys
input = sys.stdin.readline

def round(n):
    if n%1<0.5:
        return int(n)
    else:
        return int(n)+1

n = int(input())
data = [int(input()) for _ in range(n)]
data.sort()
cut = round(n*0.15)
data = data[cut:n-cut]

print(round(sum(data)/len(data)) if data else 0)