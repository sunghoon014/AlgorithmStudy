import sys

input = sys.stdin.read
data = input().splitlines()
N = int(data[0])

nums = []
for i in range(1, N + 1):
    nums.append(int(data[i]))

nums.sort()
sys.stdout.write('\n'.join(map(str, nums)) + '\n')