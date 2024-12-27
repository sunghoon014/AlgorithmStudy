# 15903 카드 합체 놀이
import heapq
n,m=map(int,input().split()) # n : 1,000 m : 15,000
cards=list(map(int,input().split())) #  1,000,000
heapq.heapify(cards)
for _ in range(m):
    popped_1=heapq.heappop(cards)
    popped_2=heapq.heappop(cards)
    temp=popped_1+popped_2
    heapq.heappush(cards,temp)
    heapq.heappush(cards,temp)

print(sum(cards))