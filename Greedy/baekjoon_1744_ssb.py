n = int(input())
data = [int(input()) for _ in range(n)]

# (양, 양) / x(양, 0)x / x(양, 음)x / (0, 음) / (음, 음)
# '양' 중에서도 1은 무조건 더하기 -> 데이터를 0보다 큰 리스트 / 0보다 작거나 같은 리스트로 나누기
# '양'은 가장 큰 것끼리 곱해야 최대가 됨 / '음'은 가장 작은 것끼리 곱해야 최대가 됨

data_plus, data_minus = [], []
for i in data:
    if i>0:
        data_plus.append(i)
    else:
        data_minus.append(i)
data_plus.sort(reverse=True)
data_minus.sort()

def cluster(data):
    i = 0
    result = []
    while i<len(data):
        if data[i]==1:
            result.append(data[i])
            i += 1
        else:
            if i<len(data)-1:
                if data[i+1]==1:
                    result.append(data[i])
                    i += 1
                else:
                    result.append(data[i]*data[i+1])
                    i += 2
            else:
                result.append(data[i])
                i += 1
    return sum(result)

print(cluster(data_plus)+cluster(data_minus))