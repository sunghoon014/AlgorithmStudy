# 11000 강의실 배정
import sys
import heapq
input=sys.stdin.readline
N=int(input())
time_table=[list(map(int,input().split()))for _ in range(N)]
time_table.sort(key=lambda x : (x[0],x[1]))
heap=[time_table[0][1]] # 종료시간 heap에 입력

for i in range(1,N):
    if heap[0]<=time_table[i][0]:
        heapq.heappop(heap)
    heapq.heappush(heap,time_table[i][1])

print(len(heap))
# print(heap)