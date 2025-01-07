l = int(input())
s = list(map(lambda x: ord(x)-ord('a')+1, list(input())))

sum = 0
for i, j in enumerate(s):
    sum += j*(31**i)

print(sum%1234567891)