# 11650 좌표 정렬하기
import sys
input=sys.stdin.readline
N=int(input())
dots=[list(map(int,input().split()))for _ in range(N)]
dots.sort(key=lambda x : (x[0],x[1]))
for points in dots:
    print(points[0],points[1])