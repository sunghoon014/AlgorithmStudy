import sys

input = sys.stdin.readline
x = int(input())

d = [0] * (x + 1)
for i in range(2, x + 1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i - 1] + 1
    # print("index", i, d[i], "에서 1을 빼는 경우", d[i - 1])
    # 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        # print("index", i, "2 나누기 몫=인덱스", i // 2)
        d[i] = min(d[i], d[i // 2] + 1)
    # 3로 나누어 떨어지는 경우
    if i % 3 == 0:
        # print("index", i, "3 나누기 몫=인덱스", i // 3)
        d[i] = min(d[i], d[i // 3] + 1)
    # print(d[i])
    # print()
# print(d[: x + 1])
print(d[x])
