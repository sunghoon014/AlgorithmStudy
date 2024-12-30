t = int(input())
for _ in range(t):
    data = int(input())
    # 13>6,1>3,0>1,1>0,1>> 1 0 1 1
    result = []
    i = 0
    while data!=0:
        data, r = divmod(data, 2)
        if r==1:
            result.append(i)
        i += 1
    print(*result)