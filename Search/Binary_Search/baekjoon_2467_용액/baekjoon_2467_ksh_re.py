import sys

input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
lst.sort()
print(lst)

start = 0
end = len(lst)


# 배열에서 뺀 값이 절대값이 가장 낮은 것을 구해라
# 입력이 음수 인 경우만 있을 수 있고 양수인 경우만 있음
# 투포인터
# 처음이랑 맨 끝을 인덱스로 두고 최소 값을 아무 수나 둠
# 두개를 더한다음에 절대 값을 최소 값보다 작으면 최소 값에 저장하고 인덱스를 저장
# 최소 값이 0이면 중단
# 최소 값이 0보다 크면 end를 한칸 땅기고, 그게 아니면 start를 땡김
