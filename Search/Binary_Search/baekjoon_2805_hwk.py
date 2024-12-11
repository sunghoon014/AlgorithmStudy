N, M = map(int, input().split())
trees = list(map(int, input().split()))
# 이진 탐색 범위 줄어드는 속도가 굉장히 빨라서
# 범위 제한 없이 그냥 바로 해도 괜찮을 것 같다.
start, end = 0, sum(trees)
answer = 0

while start <= end:
    mid = (start+end)//2
    if sum([num-mid for num in trees if num>=mid]) >= M:    # 높이 올려도 됨
        start = mid + 1
        answer = mid
    else: # 높이 낮춰야 함
        end = mid - 1
print(answer)