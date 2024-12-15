from bisect import bisect_left, bisect_right
N = int(input())
nums = sorted([int(input()) for _ in range(N)])
left, right = bisect_left(nums, 0), bisect_right(nums, 0)
zero = left if left==right else right
neg, pos = nums[:zero][::-1], nums[zero:]

def cal(list):
    answer = 0
    while list:
        num = list.pop()
        if list:    # 빈 리스트가 아닐 때
            if list[-1]==0:
                break
            # 곱한 게 더 클 때만 곱하는 게 의미 있음
            mul = num * list[-1]
            if mul > num:
                answer += mul
                list.pop()
            else:   # 1*1 같은 경우
                answer += num
        else:   # 빈 리스트일 때
            answer += num
    return answer

print(cal(neg)+cal(pos))