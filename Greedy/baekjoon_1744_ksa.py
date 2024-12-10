N = int(input())

pos = []
neg = []
one = []
zero = []

for i in range(N):
    value = int(input())
    if value > 1:
        pos.append(value)
    elif value == 0:
        zero.append(value)
    elif value == 1:
        one.append(value)
    else:
        neg.append(value)
        
pos.sort(reverse=True)
neg.sort()
sum = 0

if one:
    sum = len(one)

if pos:
    for i in range(0, len(pos)-1, 2):
        sum += pos[i]*pos[i+1]
    if len(pos) % 2 == 1:
        sum += pos[-1]
    
if neg:
    for i in range(0, len(neg)-1, 2):
        sum += neg[i]*neg[i+1]
    if len(neg) % 2 == 1:
        if not zero:
            sum += neg[-1]

print(sum)
# if len(numbers) == 1:
#     total = int(numbers[0])
# else:
#     sum = numbers[0]
#     i = 0
#     if numbers[0] < 0:
#         while sum<0 and i < len(numbers) -1:
#             sum += numbers[i]
#             i += 1

#     rest_numbers = numbers[i:]
#     rest_numbers.sort(reverse=True)

#     total = sum
#     for i in range(0, len(rest_numbers)-1, 2):
#         if i+1 < len(rest_numbers):
#             mult = rest_numbers[i] * rest_numbers[i+1]
#             total += mult
#     if len(rest_numbers) % 2 == 1:
#         total += rest_numbers[-1]
    
# print(total)