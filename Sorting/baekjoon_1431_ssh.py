import sys

input = sys.stdin.read
data = input().splitlines()
N = int(data[0])

numbers = []
for i in range(1, N+1):
    number = data[i]
    sum_of_num = 0
    for letter in number:
        if '0' <= letter and letter <= '9':
            sum_of_num += int(letter)
    numbers.append([number, sum_of_num])

numbers.sort(key=lambda x: (len(x[0]), x[1], x[0]))

for number, _ in numbers:
    print(number)