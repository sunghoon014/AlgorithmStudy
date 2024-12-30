t = int(input())
for _ in range(t):
    a = list(input())
    b = list(input())
    distance = 0
    for i, j in zip(a, b):
        if i!=j:
            distance += 1
    print(f'Hamming distance is {distance}.')