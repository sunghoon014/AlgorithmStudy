# 1431 시리얼 번호
# 32412 KB 36ms
import sys
input=sys.stdin.readline
N=int(input())
guitar_list=[]
for _ in range(N):
    tmp_num=0
    serial_code=input().strip()
    for char in serial_code:
        if char.isdigit():
            tmp_num+=int(char)
    guitar_list.append([serial_code,tmp_num]) # 메모리 더 잡아먹음 145C [145C,10]
guitar_list.sort(key=lambda x : (len(x[0]),x[1],x[0]))
for guitar,num in guitar_list:
    print(guitar)

# # 31120 KB 36ms
# N=int(input())
# guitar_list=[input() for _ in range(N)]

# def check_number(string):
#     number_sum=0
#     for char in string:
#         if char.isdigit():
#             number_sum+=int(char)
            
#     return number_sum
        

# guitar_list.sort(key=lambda x : (len(x),check_number(x),x))



# for ans in guitar_list:
#     print(ans)
