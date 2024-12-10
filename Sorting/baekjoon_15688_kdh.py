# 15688 수 정렬하기 5
import sys
input=sys.stdin.readline
N=int(input())
arr=[int(input())for _ in range(N)]
arr.sort()
for num in arr:
    print(num)