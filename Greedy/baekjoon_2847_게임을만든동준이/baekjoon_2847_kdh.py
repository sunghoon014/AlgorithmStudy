# 2847 게임을 만든 동준이
N=int(input())
score_list=[[level,int(input())]for level in range(N)]
score_list.sort(key=lambda x : x[0])
# 점수를 무조건 증가하게 만들어야 함
cnt=0
for idx in range(N-1,0,-1):
    if score_list[idx][1]>score_list[idx-1][1]:
        continue
    elif score_list[idx][1]==score_list[idx-1][1]:
        score_list[idx-1][1]-=1
        cnt+=1
    else:
        tmp=(score_list[idx-1][1]-score_list[idx][1])
        score_list[idx-1][1]-=(tmp+1)
        cnt+=(tmp+1)

print(cnt)
# print(score_list)