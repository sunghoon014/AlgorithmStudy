result = []
for i in range(10):
    data = int(input())
    result.append(data%42)
print(len(set(result)))