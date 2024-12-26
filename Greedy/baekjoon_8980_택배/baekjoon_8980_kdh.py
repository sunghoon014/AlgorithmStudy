# 8980 택배
N,C=map(int,input().split()) #C : capacity of truck
info=int(input())
box_info=[list(map(int,input().split()))for _ in range(info)]

box_info.sort(key=lambda x : x[1])
truck=[]
ans=0

capcity=[C]*(N+1)

for src,dst,weight in box_info:
    loaded_weight=C
    for i in range(src,dst): 
        # 출발지와 도착지 사이에 배달 가능한 용량만큼만 적재가능 ex) capacity : 30_(1) 60_(2) "20_(3)" 60_(4) 60_(5) 60_(6) 인 경우,
        # 2에서 5까지 배달을 한다면, 2,3,4 위치에서 최소 값까지만 적재 가능함(5는 어차피 내려서 상관없음). (20) 실제로 70이여도 20만 트럭에 적재할 수 있음
        if loaded_weight>min(capcity[i],weight): # 현재 박스의 정보와, 가는길에 있는 남은 적재 가능 용량과 비교하여 최소 값만 load할 수 있다.
            loaded_weight=min(capcity[i],weight)
    for i in range(src,dst):
        capcity[i]-=loaded_weight # load한 무게 만큼 가는길에 적재 가능 용량은 모두 감소를 시킬것.
    ans+=loaded_weight

print(ans)