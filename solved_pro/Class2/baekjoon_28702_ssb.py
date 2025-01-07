for i in range(3):
    data = input()
    if data.isnumeric():
        data = int(data)
        j = data + 3 - i

if j%3==0 and j%5==0:
    print('FizzBuzz')
elif j%3==0:
    print('Fizz')
elif j%5==0:
    print('Buzz')
else:
    print(j)