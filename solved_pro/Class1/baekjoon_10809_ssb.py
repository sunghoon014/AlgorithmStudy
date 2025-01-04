lst = [-1 for _ in range(26)]

s = list(input())
for i in range(len(s)):
    if lst[ord(s[i])-ord('a')] != -1:
        continue
    else:
        lst[ord(s[i])-ord('a')] = i
print(*lst)