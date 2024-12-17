# 1744 수 묶기
import bisect
N=int(input())
num_list=list(int(input())for _ in range(N))
num_list.sort()

minus_idx=[]
plus_idx=[]
for idx,number in enumerate(num_list):
    if number<=0:
        minus_idx.append(idx)
    else:
        plus_idx.append(idx)

# print(f'minux_idx{minus_idx}')
# print(f'plus_idx{plus_idx}')

minus_result=0
plus_result=0

if len(minus_idx)!=0:
    minus_i=minus_idx[0]
    while minus_i<=minus_idx[-1]:
        if minus_i+1<len(num_list) and num_list[minus_i+1]<=0:
            minus_result+=num_list[minus_i]*num_list[minus_i+1]
            minus_i+=2
        else:
            minus_result+=num_list[minus_i]
            minus_i+=1

if len(plus_idx)!=0:
    plus_i=plus_idx[-1]
    while plus_i>=plus_idx[0]:
        # print((plus_i,plus_result))
        
        if plus_i-1>=0 and num_list[plus_i-1]>0 and num_list[plus_i-1]!=1:
            plus_result+=num_list[plus_i]*num_list[plus_i-1]
            plus_i-=2
        else:
            plus_result+=num_list[plus_i]
            plus_i-=1

# print(f'plus_sum:{plus_result},minus_sum:{minus_result}')
# print(f'final_result{plus_result+minus_result}')
print(plus_result+minus_result)