# 16401 과자 나눠주기
M,N=map(int,input().split())
snack_list=list(map(int,input().split()))
snack_list.sort()
left=1
right=snack_list[-1]
def binary_search(M,left,right):
    if left>right:
        return right
    mid=(left+right)//2
    cnt=0
    for snack in snack_list:
        cnt+=snack//mid
    if cnt==M:
        return binary_search(M,mid+1,right)
    elif cnt>M:
        return binary_search(M,mid+1,right)
    else:
        return binary_search(M,left,mid-1)

print(binary_search(M,left,right))