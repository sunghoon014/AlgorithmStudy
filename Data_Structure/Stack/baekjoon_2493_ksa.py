#탑의 수
N = int(input())
tower = list(map(int, input().split())) #타워 높이 리스트
stack = []
output = [0] * N

for i in range(N): #탑 개수 만큼
    # 스택에 값이 있는 동안(=왼쪽에 탑이 있음) 
    # 스택의 top보다 현재 탑 i 높이가 크거나 같은 동안
    while stack and tower[stack[-1]] <= tower[i]:
        stack.pop()
    if stack: #스택에 값이 있다 = 수신할 탑이 있다
        output[i] = stack[-1] + 1
        
    stack.append(i)
print(*output)

#5 6 5 7 4
#[3]
#0 0 2 0 4