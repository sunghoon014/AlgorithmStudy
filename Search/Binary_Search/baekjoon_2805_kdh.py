# 2805 나무자르기
N,M=map(int,input().split())
tree_list=list(map(int,input().split()))
tree_list.sort()
left=1
right=tree_list[-1]
def binary_search(M,left,right):
    if left>right:
        return right
    mid=(left+right)//2
    temp_sum=0
    for tree in tree_list:
        if tree>=mid:
            temp_sum+=(tree-mid)
        else:
            continue
    if temp_sum>=M:
        return binary_search(M,left=mid+1,right=right)
    else:
        return binary_search(M,left=left,right=mid-1)

print(binary_search(M,left,right))
