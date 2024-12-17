data = list(input())

dic = []
for i in range(len(data)):
    dic.append(''.join(data[i:]))

dic.sort()
for i in dic:
    print(i)