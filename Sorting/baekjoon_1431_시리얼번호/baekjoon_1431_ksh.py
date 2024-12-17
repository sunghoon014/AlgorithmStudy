import sys

input = sys.stdin.readline

n = int(input())
lst = [str(input()) for _ in range(n)]


def custom_sum(string):
    result = 0
    for x in string:
        try:
            result += int(x)
        except:
            continue
    return result


result = []
for l in lst:
    f = len(l.strip())
    s = custom_sum(l.strip())
    result.append([f, s, l.strip()])

result.sort(key=lambda x: (x[0], x[1], x[2]))

for r in result:
    print(r[-1])
