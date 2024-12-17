# 10814 나이순 정렬
import sys
input=sys.stdin.readline
N=int(input())
participate=[list(input().split())for _ in range(N)]
participate.sort(key= lambda x : int(x[0]))
# print('--anwer--')
for person in participate:
    print(' '.join(person))
