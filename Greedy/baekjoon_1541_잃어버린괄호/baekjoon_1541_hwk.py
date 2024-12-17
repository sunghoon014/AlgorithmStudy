# - 사이에 있는 애들 모두 더하기. 그러면 엄청 큰 수가 음수가 됨
nums = []
ops = []
string = input()
answer = 0
sign = 1
num = ""
for i in range(len(string)):
    str = string[i]
    if str not in ["+", "-"]:
        num += str
    else:
        v = int(num)
        answer += v*sign
        if str=="-" and sign==1: sign=-1
        num = ""
print(answer+int(num)*sign)
