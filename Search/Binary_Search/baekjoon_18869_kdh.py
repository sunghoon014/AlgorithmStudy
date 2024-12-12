# 18869 멀티버스 2
import sys
from collections import defaultdict
input=sys.stdin.readline
M,N=map(int,input().split())
universe_info=defaultdict(int)
for _ in range(M):
    planets=list(map(int,input().split()))
    sorted_planets=sorted(list(set(planets)))
    
    size={sorted_planets[i]:i for i in range(len(sorted_planets))} # size별로 idx 지정

    size_order=tuple([size[planet] for planet in planets])
    universe_info[size_order]+=1
#     print(size)
#     print(size_order)

# print(universe_info)
answer=0
for size_order,amount in universe_info.items():
    answer+=(amount*(amount-1))//2 # nC2

print(answer)