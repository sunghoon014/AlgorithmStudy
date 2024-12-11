import sys
import bisect
N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
A.sort()

# for i in arr:
#     pos = bisect.bisect_left(A, i)
#     if pos < len(A) and A[pos] == i:
#         print(1)
#     else:
#         print(0)  

for i in arr:
  if A[bisect.bisect(A,i)-1]==i :
    print(1)
  else:
    print(0)
    

'''
#반복문

import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split())) #이게 A 안에 있는지 검사

A.sort()

for num in arr:
    left, right = 0, N - 1
    isExist = False

    while left <= right:
        mid = (left + right) // 2
        if num == A[mid]:
            isExist = True
            break
        elif num > A[mid]:
            left = mid + 1
        else:
            right = mid - 1

    print(int(isExist))
'''

'''
#재귀

import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

A.sort()

def binary_search(num, left, right):
   if left > right:
       return False
   
   mid = (left + right) // 2
   
   if num == A[mid]:
       return True
   elif num > A[mid]:
       return binary_search(num, mid + 1, right)
   else:
       return binary_search(num, left, mid - 1)

for num in arr:
   print(int(binary_search(num, 0, N - 1)))
'''