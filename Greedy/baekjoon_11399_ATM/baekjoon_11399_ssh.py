import sys

input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
times = [ int(time) for time in data[1].split() ]
times.sort()

total = 0
now = 0
for time in times:
    now += time
    total += now 

sys.stdout.write(str(total))