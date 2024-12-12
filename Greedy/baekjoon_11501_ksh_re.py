import sys

input = sys.stdin.readline


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
        if custom_search(n_lst, n_lst[i], i + 1):
            lst.append(n_lst[i])
        elif (n_lst[i] > n_lst[i + 1]) and (len(lst) > 0):
            for x in lst:
                result += n_lst[i] - x
            lst = []

    for x in lst:
        result += n_lst[-1] - x

    print(result)
