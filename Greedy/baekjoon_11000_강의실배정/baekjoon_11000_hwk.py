# 1. heap에 하나씩 넣으면서 heap에 있는 강의 중 가장 끝나는 강의와 다음 배정할 강의를 비교해서
# 같은 강의실에서 계속 수업이 가능한지, 아니면 새 강의실을 파야하는지를 판단해야 함
# 2. heap 안에 있는 강의 수는 필요한 강의실 개수이고, heap 특성을 이용해 현 시점 가장 빨리 끝나는 강의 시간을 얻는다.
# 가장 빨리 끝나는 강의와 새 강의의 시작시간을 비교해서 가장 빨리 끝나는 강의실에조차 새 강의가 배정될 수 없다면
# 그 뒤에 끝나는 다른 강의실에도 배정되지 못할 게 당연하므로 더 비교하지 않고 강의실을 새로 파는 원리
# 3. 만약 가장 빨리 끝나는 강의실에서 이어서 강의할 수 있다면 새 강의를 그 회의실에 넣어 줌
# 이걸 heappop으로 구현
import heapq
N = int(input())
classes = [tuple(map(int, input().split())) for _ in range(N)]
classes.sort()
heap = [classes[0][1]]

for i in range(1, N):
    if heap[0] <= classes[i][0]:
        heapq.heappop(heap)
    heapq.heappush(heap, classes[i][1])

print(len(heap))