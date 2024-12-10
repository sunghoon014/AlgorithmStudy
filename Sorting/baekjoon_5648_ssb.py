inputs = []
n = -1
while len(inputs) != n:
    datas = input().split()
    if len(inputs) == 0:
        n = int(datas[0])
        for data in datas[1:]:
            inputs.append(int(data[::-1]))
    else:
        for data in datas:
            inputs.append(int(data[::-1]))

inputs.sort()
for i in inputs:
    print(i)