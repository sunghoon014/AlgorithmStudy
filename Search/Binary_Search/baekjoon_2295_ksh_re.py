import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]
lst_de = deque(lst[::-1])

while True:
    x = lst_de.popleft()

    result = 0
    for l1 in lst_de:
        for l2 in lst_de:
            if l1 != l2:
                for l3 in lst_de:
                    if (l2 != l3) and (l1 != l3):
                        if l1 + l2 + l3 == x:
                            result = l1 + l2 + l3
                            break

    if x == result:
        break

print(result)
