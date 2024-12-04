import sys
input = sys.stdin.readline

n = int(input())

result = []
for _ in range(n):
    instance = int(input())
    if instance != 0:
        result.append(instance)
    else:
        result.pop(-1)
        
print(sum(result))