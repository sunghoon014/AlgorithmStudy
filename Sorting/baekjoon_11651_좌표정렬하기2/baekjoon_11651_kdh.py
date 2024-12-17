# 11650 좌표 정렬하기 2
import sys
input=sys.stdin.readline
N=int(input())
dots=[list(map(int,input().split()))for _ in range(N)]
dots.sort(key=lambda x : (x[1],x[0]))
for points in dots:
    print(points[0],points[1])