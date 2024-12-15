# 1654 랜선자르기
K,N=map(int,input().split())
line_list=[int(input()) for _ in range(K)]
line_list.sort()
left=1
right=line_list[-1]
# 1~802
while left<=right:
    mid=(left+right)//2
    lane=0

    for line in line_list:
        lane+=line//mid

    if lane==N: # 당장에 N만큼 만들 수 있어도, 더 긴 길이가 가능하다.
        left=mid+1

    elif lane>N:
        left=mid+1
    
    elif lane<N:
        right=mid-1

print(right)

