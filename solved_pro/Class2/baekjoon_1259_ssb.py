data = input()
while data!='0':
    data = list(data)
    n = len(data)
    if data[:n//2] == data[n+1:(n-1)//2:-1]:
        print('yes')
    else:
        print('no')
    data = input()