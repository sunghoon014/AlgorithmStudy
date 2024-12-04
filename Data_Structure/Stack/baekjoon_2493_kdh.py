# 2493 탑
N=int(input())
tower_heights=list(map(int,input().split()))
result=[0]*N
tong=[(0,tower_heights[0])]
popped_result=[]
# 이전 index의 값이 더 작으면(왼쪽 빌딩의 크기가 더 작으면) push
for curr_idx in range(1,N):
    curr_height=tower_heights[curr_idx]
    while tong:
        # print(f'height:{curr_height},idx:{curr_idx},status:{tong}')
        if tong[-1][1]>curr_height:
            result[curr_idx]=tong[-1][0]+1
            break
        else:
            tong.pop()
    tong.append((curr_idx,curr_height))

print(*result)