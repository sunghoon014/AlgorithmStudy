import sys

input = sys.stdin.readline


# 재귀 횟수가 길어져서
def custom_search(n_lst, n, idx):
    if idx == len(n_lst):
        return False
    if n <= n_lst[idx]:
        return True

    return custom_search(n_lst, n, idx + 1)


T = int(input())
for _ in range(T):
    N = input()
    n_lst = list(map(int, input().split()))

    lst = []
    result = 0
    for i in range(len(n_lst) - 1):
        # 다음 날들 중에 기준 날보다 더 큰 값이 있을 경우 True
        if custom_search(n_lst, n_lst[i], i + 1):
            lst.append(n_lst[i])

        # 가격이 떨어지는 경우와 lst안에 요소가 있을 경우 가격 계산
        elif (n_lst[i] > n_lst[i + 1]) and (len(lst) > 0):
            for x in lst:
                result += n_lst[i] - x
            lst = []

    # 맨 마지막 가격 계산
    for x in lst:
        result += n_lst[-1] - x

    print(result)
