# 2910 빈도정렬
from collections import defaultdict
N,C=map(int,input().split())
string=input().split()
num_dict=defaultdict(int)
for num in string:
    try:
        num_dict[int(num)]+=1
    except:
        continue
sorted_num=sorted(num_dict.items(),key=lambda x : -x[1])
for num,cnt in sorted_num:
    for _ in range(cnt):
        print(num,end=' ')