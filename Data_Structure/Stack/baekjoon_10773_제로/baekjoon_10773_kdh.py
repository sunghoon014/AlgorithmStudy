# 10773 제로
N=int(input())
tong=[]
for _ in range(N):
    a=int(input())
    if a!=0:
        tong.append(a)
    else:
        tong.pop()

print(sum(tong))