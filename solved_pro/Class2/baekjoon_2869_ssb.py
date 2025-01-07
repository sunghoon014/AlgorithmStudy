import math

a, b, v = map(int, input().split())

haru = a-b
# day = math.ceil((v-a)/haru)
# if haru*day+a >= v:
#     day += 1
day = math.ceil((v-a)/haru) + 1

print(day)