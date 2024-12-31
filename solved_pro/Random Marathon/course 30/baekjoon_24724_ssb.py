import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    a, b = map(int, input().split())
    parts = [tuple(map(int, input().split())) for _ in range(n)]
    print(f'Material Management {i+1}')
    print(f'Classification ---- End!')

# for i in range(t):
#     print(f'Material Management {i+1}')
#     print(f'Classification ---- End!')