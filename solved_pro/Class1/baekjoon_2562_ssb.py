max = 0
for i in range(1, 10):
    data = int(input())
    if data>max:
        max = data
        index = i

print(max)
print(index)