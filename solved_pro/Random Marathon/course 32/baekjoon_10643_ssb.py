pizza = [int(input()) for _ in range(8)]
pizza = pizza*2

max = 0
for i in range(8):
    p = sum(pizza[i:i+4])
    if max<p:
        max = p

print(max)