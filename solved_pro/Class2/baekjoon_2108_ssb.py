import sys
input = sys.stdin.readline

n = int(input())
data = [int(input()) for _ in range(n)]
data.sort()

def round(n):
    abs(n)
    if n>=0:
        return int(n) if n%1<0.5 else int(n)+1
    else:
        return int(n) if abs(n)%1<0.5 else int(n)-1
    
print(round(sum(data)/n))
print(data[n//2])

from collections import defaultdict
dict = defaultdict(int)
for d in data:
    dict[d] += 1

dict = sorted(dict.items(), key=lambda x: (-x[1], x[0]))
if len(dict)>1:
    print(dict[1][0] if dict[0][1] == dict[1][1] else dict[0][0])
else:
    print(dict[0][0])
print(max(data)-min(data))