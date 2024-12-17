# 1931 회의실 배정
N=int(input())
time_table=[list(map(int,input().split()))for _ in range(N)]
cur_end=0
result=0
time_table.sort(key=lambda x :(x[1],x[0]))
for start,end in time_table:
    if cur_end<=start:
        cur_end=end
        result+=1
print(result)