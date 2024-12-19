import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]
lst.sort(reverse=True)

lst = deque(lst)
flag = False
result = 0
while True:
    if len(lst) < 1:
        break

    # 모두 음수만 남았으니 반전
    if (flag == False) and (lst[0] < 0) and len(lst) > 1:
        lst = deque(list(lst)[::-1])
        flag = True

    l = lst.popleft()

    # 가장 큰 양수 묶어서 곱하기
    if (len(lst) > 0) and (l > 1) and (lst[0] > 1):
        l2 = lst.popleft()
        result += l * l2

    # 음수 끼리 묶어서 곱하기
    elif (len(lst) > 0) and (l < 0) and (lst[0] < 0):
        l2 = lst.popleft()
        result += l * l2

    # 음수가 1개이고 0이 있다면 결합
    elif (len(lst) == 1) and (l == 0) and (lst[0] < 0):
        l2 = lst.popleft()
        result += l * l2

    # 음수가 홀수개이고 0이 있다면 결합
    elif (len(lst) > 1) and (len(lst) % 2 == 1) and (l == 0) and (lst[0] < 0):
        l2 = lst.popleft()
        result += l * l2
    else:
        result += l

print(result)
