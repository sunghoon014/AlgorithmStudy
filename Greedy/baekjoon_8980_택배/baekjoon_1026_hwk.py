# 트럭을 최대한 꽉꽉 채우면서 배달 거리가 짧은 택배들 우선으로 배달하는 것이 가장 많은 택배를 배달하는 방법
# 배달은 순방향으로 진행되니까 배달 거리가 짧은 것에만 초점을 맞추면 중간에 트럭에 택배를 싣지 않은 구간이 나타날 수도 있기 때문에 도착지가 가까운 곳도 고려해야 함
# 도착지 기준으로 오름차순하고, 하나씩 꺼내어 시작지부터 도착지까지 훑어보며 이 구간동안 이 택배를 최대 몇 개를 실을 수 있을지 판단
# 시작지부터 도착지까지 실을 택배가 이미 있는 경우 남은 용량만큼만 실어야 함

N, C = map(int, input().split())
M = int(input())
packs = [list(map(int, input().split())) for _ in range(M)]
packs.sort(key=lambda x:x[1])
capacity = [C]*(N+1)    # 각 도시에서 트럭에 담긴 택배 수
answer = 0
for fr, to, num in packs:
    min_v = C   # 이 구간에서 이 택배 몇 개 실을지
    # 도시를 돌면서 각 도시에서 남은 트럭 용량을 보면서 최대 몇 개 실을지 판단
    for i in range(fr, to):
        temp = min(capacity[i], num)
        min_v = min(min_v, temp)
    # 택배 싣기
    for i in range(fr, to):
        capacity[i] -= min_v
    answer += min_v
print(answer)