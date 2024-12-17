import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

t_lst = [list(map(int, input().split())) for _ in range(n)]
t_lst_len = [[l[0], l[1], l[1] - l[0]] for l in t_lst]
t_lst_len.sort(key=lambda x: (x[0], x[-1]))
t_lst_len = deque(t_lst_len)

max_c = 0
while True:
    if len(t_lst_len) < 1:
        break
    c = 1
    lst = t_lst_len.popleft()
    s, e, l = lst[0], lst[1], lst[2]
    if l == 0:
        c += 1

    for _lst in t_lst_len:
        if e < _lst[0]:
            c += 1
            s = _lst[0]
            e = _lst[1]

    max_c = max(max_c, c)

print(max_c)

"""
종료시간 기준으로 sorting
종료시간이 최대한 빠르면 먼저 회의를 하고, 그다음에 종료시간이 빠른 것중에 시작할 수있는 것을 시작해야한다
"""
