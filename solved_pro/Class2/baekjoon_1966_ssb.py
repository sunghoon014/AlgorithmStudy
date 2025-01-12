from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    queue = deque([(i, j) for i, j in enumerate(map(int, input().split()))])
    cnt = 0
    while True:
        i, j = queue.popleft()
        if any(p > j for _, p in queue):
            queue.append((i, j))
        else:
            cnt += 1
            if i == m:
                print(cnt)
                break