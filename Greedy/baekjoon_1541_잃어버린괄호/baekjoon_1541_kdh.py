# 1541 잃어버린 괄호
string=input().split(sep='-')
result=0
for idx,number in enumerate(string):
    if len(number.split(sep='+'))>1:
        for temp_num in number.split(sep='+'):
            if idx>=1:
                result-=int(temp_num)
            else:
                result+=int(temp_num)
    else:
        if idx>=1:
            result-=int(number)
        else:
            result+=int(number)
print(result)