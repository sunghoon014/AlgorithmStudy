# 11652 카드
from collections import defaultdict
import sys
input=sys.stdin.readline
N=int(input())
number_dic=defaultdict(int)
for _ in range(N):
    number_dic[int(input())]+=1

sorted_dic=sorted(number_dic.items(),key=lambda x : (x[1],-x[0]),reverse=True)

print(sorted_dic[0][0])