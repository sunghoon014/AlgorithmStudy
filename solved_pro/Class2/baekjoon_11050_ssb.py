n, k = map(int, input().split())

top = 1
for i in range(n, n-k, -1):
    top *= i

down = 1
for j in range(1, k+1):
    down *= j

print(top//down)