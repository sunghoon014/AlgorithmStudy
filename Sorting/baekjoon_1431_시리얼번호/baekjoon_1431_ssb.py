n = int(input())

serial_info = []
for i in range(n):
    data = input()
    num = 0
    for chr in data:
        if chr.isnumeric():
            num += int(chr)
    serial_info.append([data, num])

serial_info.sort(key=lambda x: (len(x[0]), x[1], x[0]))
for serial in serial_info:
    print(serial[0])