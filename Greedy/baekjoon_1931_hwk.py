N = int(input())
scheds = [] # 모든 신청 스케쥴 모음
for _ in range(N):  # 신청 스케쥴들 취합
    start, end = map(int, input().split())
    scheds.append((start, end))
scheds.sort()   # 시작 시간 순서대로 정렬
answer = 0
cur_start, cur_end = 0, 0
# 스케쥴을 하나씩 가져와서 현재 배치한 제일 마지막 스케쥴과 끝나는 시간끼리 비교
# 현재 가져온 스케쥴이 배치된 제일 마지막 스케쥴보다 일찍 끝나면 스케쥴 교체
# 현재 가져온 스케쥴이 배치된 제일 마지막 스케쥴보다 늦게 끝나면 시작 시간끼리 비교
# 현재 가져온 스케쥴이 배치된 제일 마지막 스케쥴이 끝난 뒤에 시작할 경우 새로 배치
# 위 경우 모두 해당하지 않은 경우 무시
for i in range(len(scheds)):
    start, end = scheds[i]
    if cur_end > end:
        cur_start = start
        cur_end = end
    elif cur_end <= start:
        cur_start = start
        cur_end = end
        answer += 1
print(answer)