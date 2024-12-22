data = list(map(int, input().split()))
while data!=[0, 0, 0]:
    data.sort()
    a, b, c = data
    if c**2==a**2+b**2:
        print('right')
    else:
        print('wrong')
    data = list(map(int, input().split()))