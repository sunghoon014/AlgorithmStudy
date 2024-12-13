import sys
input = sys.stdin.readline

N = int(input())
numbers = [int(input()) for _ in range(N)]

numbers.sort(reverse=True)

possible = set()

for i in range(N):
    for j in range(N):
        for k in range(N):
            sum = numbers[i] + numbers[j] + numbers[k]
            if sum in numbers:
                possible.add(sum)
                
print(max(possible))