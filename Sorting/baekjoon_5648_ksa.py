first = input().split()
n = int(first[0])
numbers = list(map(int, first[1:]))

while len(numbers) < n:
    numbers.extend(map(int, input().split()))
    
def reverse_num(num):
    return int(str(num)[::-1])

reversed_num = [reverse_num(num) for num in numbers]

for num in sorted(reversed_num):
    print(num)