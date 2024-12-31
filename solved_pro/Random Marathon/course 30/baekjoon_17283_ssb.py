l = int(input())
r = int(input())

i = 1
sum = 0
while True:
    l = int(l*(r/100))
    if l<=5:
        break
    else:
        sum += l*(2**i)
    i += 1

print(sum)