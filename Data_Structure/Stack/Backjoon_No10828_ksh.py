import sys
input = sys.stdin.readline

n = int(input())

result = []
for _ in range(n):
    instance = input().strip().split()
    # print(instance, result)
    if instance[0] == 'push':
        result.append(int(instance[1]))
    elif instance[0] == 'pop':
        if len(result) > 0:
            print(result.pop(-1))
        else:
            print(-1)
    elif instance[0] == 'size':
        print(len(result))
    elif instance[0] == 'empty':
        if len(result) > 0:
            print(0)
        else:
            print(1)
    
    elif instance[0] == 'top':
        if len(result) > 0:
            print(result[-1])
        else:
            print(-1)