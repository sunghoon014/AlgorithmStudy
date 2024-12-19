from collections import deque
N, K = map(int, input().split())

if N==K: print(0)
else:
    que = deque([N])
    visited = [0]*int(1e6+1)
    while que:
        pos = que.popleft()
        for new_pos in [pos-1, pos+1, pos*2]:
            if not 0<=new_pos<=int(1e6) or visited[new_pos]: continue
            que.append(new_pos)
            visited[new_pos]=visited[pos]+1
            if new_pos==K:
                print(visited[new_pos])
                exit()