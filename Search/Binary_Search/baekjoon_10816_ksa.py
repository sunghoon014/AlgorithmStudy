import sys
from bisect import bisect_left,  bisect_right

N = int(sys.stdin.readline())
card= list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
cnt = list(map(int, sys.stdin.readline().split()))
ans = []
card.sort()

for i in cnt:
    left = bisect_left(card, i)
    right = bisect_right(card, i)
    ans.append(int(right-left))
print(*ans)