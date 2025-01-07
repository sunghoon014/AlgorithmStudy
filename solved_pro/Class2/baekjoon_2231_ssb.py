str_n = input()
n = int(str_n)

num = 0
for i in range(n+1):
    if n == i + sum(map(int, list(str(i)))):
        num = i
        break
    
print(num)