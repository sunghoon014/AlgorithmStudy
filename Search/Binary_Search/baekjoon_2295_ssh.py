import sys

N = int(sys.stdin.readline())
numbers = [ int(sys.stdin.readline()) for _ in range(N) ]
numbers.sort()

sum_nums = [ numbers[i] + numbers[j] for i in range(0, N) for j in range(0, N) ]
sum_nums = set(sum_nums)

for i in range(N-1, -1, -1):
    for j in range(i+1):
        if numbers[i] - numbers[j] in sum_nums:
            print(numbers[i])
            sys.exit()