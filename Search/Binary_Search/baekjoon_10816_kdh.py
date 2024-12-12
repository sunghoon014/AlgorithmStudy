# 10816 숫자 카드2
import bisect
import sys
input=sys.stdin.readline
N=int(input())
cards=list(map(int,input().split()))
cards.sort()
M=int(input())
own_cards=list(map(int,input().split()))
result=[]
for own in own_cards:
    if cards[bisect.bisect(cards,own)-1]==own:
        result.append(bisect.bisect_right(cards,own)-bisect.bisect_left(cards,own))
    else:
        result.append(0)
print(*result)