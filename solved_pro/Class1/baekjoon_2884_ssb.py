# -45분 = -1시간 +15분
h, m = map(int, input().split())
h, m = h-1, m+15
if m>59:
    h += 1
    m -= 60
if h<0:
    h += 24
result = [h, m]
print(*result)