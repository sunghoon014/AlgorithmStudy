import numpy as np

t = int(input())
result = []
for _ in range(t):
    n = int(input())
    data = np.array(list(map(int, input().split())))
    i = 0
    money = 0
    while i!=n:
        data_now = data[i:]
        max_index = np.argmax(data_now)+i
        if max_index == i:
            i += 1
        else:
            while i!=max_index+1:
                money += data[max_index]-data[i]
                i += 1
    result.append(money)

for value in result:
    print(value)