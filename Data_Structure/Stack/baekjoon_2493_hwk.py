n = int(input())
lazers = list(map(int, input().split()))
stack = []
indexs = [0]*n  # 각 빌딩의 레이저가 닿는 건물의 인덱스

# 현재 주목하고 있는 건물 왼쪽에 있는 건물들 중 현재 건물의 높이 보다 높거나 같은 건물들만 남기는 방식
for idx, lazer in enumerate(lazers):
    while stack and stack[-1][-1]<=lazer:  # 현재 건물보다 낮은 건물들 다 pop
        stack.pop()
    if stack:  # 남아 있는 건물 중 가장 가까운 건물이 레이저가 닿는 건물
        indexs[idx] = stack[-1][0]
    stack.append((idx+1, lazer))

print(*indexs)
