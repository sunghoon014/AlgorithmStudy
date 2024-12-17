# 2295 세수의 합
N=int(input())
U=set(int(input())for _ in range(N)) # U 집합 선언
sum_U=set()
for i in U:
    for j in U:
        sum_U.add(i+j)

answer_list=[]
# x+y+z=k -> x+y=k-z (x,y,k,z 모두 U집합 안에 있음)
for k in U:
    for z in U:
        if k-z in sum_U:
            answer_list.append(k)

print(sorted(answer_list)[-1])