'''
import sys
input = sys.stdin.readline

lenA, lenB = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

onlyA = A - B
onlyA = sorted(onlyA)

print(len(onlyA))
if onlyA:
    print(*onlyA)
'''

import sys
from bisect import bisect_left
input = sys.stdin.readline

lenA, lenB = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B.sort()
onlyA = []
for num in A:
    tmp = bisect_left(B, num)
    if tmp >= len(B) or B[tmp] != num:
        onlyA.append(num)
        
onlyA.sort()
print(len(onlyA))
if onlyA:
    print(*onlyA)