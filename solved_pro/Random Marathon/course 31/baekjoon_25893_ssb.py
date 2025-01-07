n = int(input())
for _ in range(n):
    score = list(map(int, input().split()))
    print(*score)
    cnt = 0
    # cnt = sum(1 for s in score if s >= 10)
    for s in score:
        if s>=10:
            cnt += 1
    if cnt == 0:
        print('zilch', end="\n\n")
    elif cnt == 1:
        print('double', end="\n\n")
    elif cnt == 2:
        print('double-double', end="\n\n")
    elif cnt == 3:
        print('triple-double', end="\n\n")
    
    # 마지막 플레이어가 아닌 경우에만 빈 줄 추가
    # if i != n - 1:
    #     print()