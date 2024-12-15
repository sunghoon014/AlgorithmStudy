import sys

N = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().split()))

start, end = 0, len(numbers) - 1
start_index, end_index = 0, len(numbers) - 1
min = 2000000001

# if numbers[start] > 0:
#     print(numbers[start], numbers[start + 1])
#     sys.exit()
# elif numbers[end] < 0:
#     print(numbers[end - 1], numbers[end])
#     sys.exit()

while True:
    val = numbers[end] + numbers[start]
    val_abs = abs(numbers[end] + numbers[start])    
    if min > val_abs:
        min = val_abs
        end_index = end
        start_index = start
    if min == 0:
        break
    elif val > 0:
        end -= 1
    else:
        start += 1
    
    if start == end:
        break

# 오답: while numbers[start] <= 0 and numbers[end] >= 0
# -5 -5 1 1 10 10
    
print(numbers[start_index], numbers[end_index])