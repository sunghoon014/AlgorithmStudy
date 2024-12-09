# 그냥 소요 순서대로 정렬하면 끝인 문제
N = int(input())
Ps = list(map(int, input().split()))
Ps.sort()
answer = 0
for i in range(len(Ps)):
    answer += sum(Ps[:i+1])

print(answer)