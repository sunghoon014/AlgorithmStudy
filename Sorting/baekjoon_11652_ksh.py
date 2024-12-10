import sys

input = sys.stdin.readline

n = int(input())
lst = [int(input()) for _ in range(n)]

result_dic = {}
for l in lst:
    try:
        result_dic[l] += 1
    except:
        result_dic[l] = 0

result_dic = sorted(result_dic.items(), key=lambda x: (-x[1], x[0]))
print(result_dic[0][0])
