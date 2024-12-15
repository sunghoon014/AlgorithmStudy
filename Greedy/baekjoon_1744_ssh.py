import sys

N = int(sys.stdin.readline())

numbers = [ int(sys.stdin.readline()) for _ in range(N) ]

numbers.sort()
total = 0

while len(numbers) != 0:
    if len(numbers) == 1:
        total += numbers[0]
        break

    if numbers[1] < 0:
        total += numbers[0] * numbers[1]
        numbers.pop(0)
        numbers.pop(0)
    elif numbers[1] == 0:
        numbers.pop(0)
        numbers.pop(0)
    elif numbers[0] < 0:
        total += numbers[0]
        numbers.pop(0)

    if len(numbers) == 1:
        total += numbers[0]
        break
    elif len(numbers) == 0:
        break
    
    if numbers[-2] > 1:
        total += numbers[-1] * numbers[-2]
        numbers.pop()
        numbers.pop()
    elif numbers[-2] == 1:
        total += numbers[-1]
        numbers.pop()
    elif numbers [-2] == 0:
        total += numbers[-1]
        numbers.pop()
    elif numbers[-1] == 0:
        numbers.pop()

print(total)