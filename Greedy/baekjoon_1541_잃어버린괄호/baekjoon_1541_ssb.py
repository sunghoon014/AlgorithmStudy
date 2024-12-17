datas = input().split('-')

result = []
for data in datas:
    result.append(str(sum(map(int, data.split('+')))))

print(eval('-'.join(result)))