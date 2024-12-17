# 5648 역원소 정렬
from collections import deque
num_list=deque()

num_list.extend(input().split())
total_length=num_list.popleft()
while True:
    if len(num_list)==int(total_length):
        break
    else:
        num_list.extend(input().split())


for idx,num in enumerate(num_list):
    tmp_string=''
    for char_idx in range(len(num_list[idx])-1,-1,-1):
        tmp_string+=num_list[idx][char_idx]
    num_list[idx]=int(tmp_string)

for ans in sorted(list(num_list)):
    print(ans)