# 11656 접미사 배열
string=input()
suffix_list=[]

for idx in range(len(string)):
    temp=''
    for char_idx in range(idx,len(string)):
        temp+=string[char_idx]
    suffix_list.append(temp)

for ans in sorted(suffix_list):
    print(ans)