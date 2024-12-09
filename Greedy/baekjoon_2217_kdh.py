# 2217 로프
N=int(input())
weight_list=[int(input()) for _ in range(N)]
weight_list.sort(reverse=True)
cur_max=weight_list[0]
for idx in range(1,len(weight_list)):
    cur_max=max(weight_list[idx]*(idx+1),cur_max)

print(cur_max)