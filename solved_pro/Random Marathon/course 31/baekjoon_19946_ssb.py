n = int(input())
i = 64
while True:
    if n%2==0:
        n = n//2
        i -= 1
    else:
        break

print(i)