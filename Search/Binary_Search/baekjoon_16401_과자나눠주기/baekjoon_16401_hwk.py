M, N = map(int, input().split())
snacks = list(map(int, input().split()))
snacks.sort() # 최대, 최솟값 구하기 min,max 안쓰고 정렬해서 인덱싱 할 것
sum_snacks = sum(snacks)

if sum_snacks<M:  # 동일한 길이의 과자로 나누어 줄 수 없는 경우
    print(0)
else:   # 조카가 과자보다 많은 경우
    mok = M//N if M%N==0 else M//N+1
    start = max(1, snacks[0]//mok) # 각 과자에서 균등한 개수만큼 만들어낼 때
    end = sum_snacks//M   # 모든 과자를 합친 후 조카 수만큼 나눌 때
    answer = 0
    while start <= end:
        mid = (start+end)//2   # 탐색 지점
        if sum([num//mid for num in snacks]) >= M:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1

    print(answer)