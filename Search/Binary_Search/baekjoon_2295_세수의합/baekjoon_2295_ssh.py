import sys

N = int(sys.stdin.readline())
numbers = [ int(sys.stdin.readline()) for _ in range(N) ]
numbers.sort()

sum_nums = [ numbers[i] + numbers[j] for i in range(0, N) for j in range(0, N) ] # x + y의 모든 경우
sum_nums = set(sum_nums)

# x + y + z = k 에서 k가 최대가 되는 경우를 찾는게 문제


for i in range(N-1, -1, -1):
    for j in range(i+1):
        if numbers[i] - numbers[j] in sum_nums: # k - z = x + y
            print(numbers[i])
            sys.exit()