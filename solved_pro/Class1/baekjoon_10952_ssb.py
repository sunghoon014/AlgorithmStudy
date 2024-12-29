while True:
    data = input()
    if data=="0 0":
        break
    print(sum(map(int, data.split())))