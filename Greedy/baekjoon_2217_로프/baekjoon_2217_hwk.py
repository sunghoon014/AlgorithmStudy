# n개의 로프를 같이 쓸 때 가장 작은 장력의 로프 * 개수로 구하는 문제
N = int(input())
ropes = []
for _ in range(N):
    ropes.append(int(input()))
ropes.sort()
answer = 0
# 로프를 하나만 쓰는 경우 ~ 다 쓰는 경우 모두 살피기
for num in range(1, len(ropes)+1):
    answer = max(answer, ropes[-num]*num)
print(answer)