import sys
import heapq

input = sys.stdin.readline
n = int(input())

heap = []
for _ in range(n):
    data = int(input())
    if data==0:
        print(heapq.heappop(heap) if heap else 0)
    else:
        heapq.heappush(heap, data)