# 2초면 포문 루프 연산 2억번

import sys

input = sys.stdin.readline
N = int(input())

num = 666
cnt = 0
while True:
    if "666" in str(num):
        cnt += 1
    if cnt == N:
        print(num)
        break
    num += 1
