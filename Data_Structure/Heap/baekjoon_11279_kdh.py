# 11279 최대 힙
import heapq
import sys
input=sys.stdin.readline
heap=[]
N=int(input())
for _ in range(N):
    a=int(input().strip())
    if a==0:
        if len(heap)!=0:
            popped=heapq.heappop(heap)
            print(popped)
        else:
            print(0)
    else:
        heapq.heappush(heap,a)
