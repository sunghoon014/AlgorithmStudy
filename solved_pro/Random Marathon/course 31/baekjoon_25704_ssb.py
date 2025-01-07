n = int(input())
p = int(input())

if n<5:
    price = p
elif n>=5 and n<10:
    price = p - 500
elif n>=10 and n<15:
    price = min(p-500, p*0.9)
elif n>=15 and n<20:
    price = min(p*0.9, p-2000)
elif n>=20:
    price = min(p-2000, p*0.75)

price = max(0, int(price))
print(price)