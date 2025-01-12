n = int(input())
inputs = [list(map(int, input().split())) for _ in range(n)]

result = []
for i in range(n):
    w, h = inputs[i]
    cnt = 1
    for input in inputs:
        compare_w, compare_h = input
        if compare_w>w and compare_h>h:
            cnt += 1
    result.append(cnt)

print(*result)