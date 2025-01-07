# # 신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.
# # 예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자. 1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다. 하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.
# # 어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.
import sys

input = sys.stdin.readline
C = int(input())
N = int(input())
visited = [False] * (C + 1)
count = 0
graph = [[] for _ in range(C + 1)]
for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(v):
    global count
    visited[v] = True
    count += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


dfs(1)
print(count - 1)

"""
import sys
from collections import deque

input = sys.stdin.readline
C = int(input())
N = int(input())
graph = [[] for _ in range(C + 1)]
for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (C + 1)
queue = deque([1])
visited[1] = True
count = 0
while queue:
    current = queue.popleft()
    for neighbor in graph[current]:
        if not visited[neighbor]:
            visited[neighbor] = True
            queue.append(neighbor)
            count += 1
print(count)
"""
