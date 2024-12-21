t = int(input())
for _ in range(t):
    r, s = input().split()
    r = int(r)
    s = list(s)
    result = ''
    for i in range(len(s)):
        result += r*s[i]
    print(result)