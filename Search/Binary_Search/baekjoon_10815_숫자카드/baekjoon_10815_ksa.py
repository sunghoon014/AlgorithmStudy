import sys
import bisect

N = int(sys.stdin.readline())
card= list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

card.sort()

for i in arr:
  if card[bisect.bisect(card,i)-1]==i :
    print(1, end = ' ')
  else:
    print(0, end = ' ')