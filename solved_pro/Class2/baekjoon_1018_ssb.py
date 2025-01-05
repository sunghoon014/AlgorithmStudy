n, m = map(int, input().split())
case_1 = ['WB'*4, 'BW'*4]*4
case_2 = ['BW'*4, 'WB'*4]*4

box = [input() for _ in range(n)]

result = []
for i in range(n-8+1):
    cut_box = box[i:i+8]
    for j in range(m-8+1):
        cuted_box = list(map(lambda x: x[j:j+8], cut_box))

        cnt_1 = 0
        for i, j in zip(cuted_box, case_1):
            for s, t in zip(i, j):
                if s!=t:
                    cnt_1 += 1
        result.append(cnt_1)

        cnt_2 = 0
        for i, j in zip(cuted_box, case_2):
            for s, t in zip(i, j):
                if s!=t:
                    cnt_2 += 1
        result.append(cnt_2)

print(min(result))