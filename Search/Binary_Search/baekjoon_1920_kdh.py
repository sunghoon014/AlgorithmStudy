# 1920 수 찾기
N=int(input())
N_list=list(map(int,input().split()))
M=int(input())
M_list=list(map(int,input().split()))

N_list.sort()
# 1. loop
# for target_num in M_list:    
#     left=0
#     right=len(N_list)-1

#     while left<=right:
#         mid=(left+right)//2
#         if N_list[mid]==target_num:
#             print(1)
#             break
#         elif N_list[mid]>target_num:
#             right=mid-1
#         else:
#             left=mid+1
#     else:
#         print(0)

# 2. recursive func
# def binarySearch(array,target,left,right):

#     if left>right:
#         return 0
#     mid_idx=(left+right)//2
    
#     # print(f'target:{target},mid_idx:{mid_idx},mid_value:{array[mid_idx]}')

#     if array[mid_idx]==target:
#         return 1
#     elif array[mid_idx]<target:
#         return binarySearch(array,target,mid_idx+1,right)
#     elif array[mid_idx]>target:
#         return binarySearch(array,target,left,mid_idx-1)
#     else:
#         return 0

# for target_num in M_list:
#     print(binarySearch(N_list,target_num,0,len(N_list)-1))

# 3. bisect library
# 1 2 3 4 5
# -> 1 3 7 9 5
import bisect
for target_num in M_list:
    if N_list[bisect.bisect(N_list,target_num)-1]==target_num:
        print(1)
    else:
        print(0)
