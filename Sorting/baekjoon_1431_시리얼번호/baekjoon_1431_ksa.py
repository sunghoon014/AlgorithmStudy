import sys
N = int(sys.stdin.readline())
serial = []
for _ in range(N):
    serial.append(sys.stdin.readline().strip())
def sum_num(x):
    sum = 0
    for i in x:
        if i.isdigit():
            sum += int(i)
    return sum
    
serial.sort(key=lambda x: (len(x), sum_num(x), x))

for i in serial:
    print(i)