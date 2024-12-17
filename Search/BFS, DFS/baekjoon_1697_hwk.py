from collections import deque
N, C = map(int, input().split())
que = deque([(N, 0)])
while C:
    pos, time = que.popleft()
    
    new_pos = pos-1
    if new_pos==C:
        print(time + 1)
        break
    que.append((new_pos, time+1))
    
    new_pos = pos+1
    if new_pos==C:
        print(time + 1)
        break
    que.append((new_pos, time+1))
    
    new_pos = pos*2
    if new_pos==C:
        print(time + 1)
        break
    que.append((new_pos, time+1))