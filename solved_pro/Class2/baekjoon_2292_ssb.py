# 1 + 6 + 12 + 18 + ..
n = int(input())

m = 1
cnt = 0
while m<n:
    m = m + 6*cnt
    cnt += 1
print(cnt if cnt else 1)