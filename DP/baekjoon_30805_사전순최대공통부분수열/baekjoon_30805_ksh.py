import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

# dp = [[[] for _ in range(M + 1)] for _ in range(N + 1)]  # DP 테이블 초기화

# for i in range(1, N + 1):
#     for j in range(1, M + 1):
#         if A[i - 1] == B[j - 1]:  # A[i]와 B[j]가 같은 경우
#             dp[i][j] = dp[i - 1][j - 1] + [A[i - 1]]
#         else:  # A[i]와 B[j]가 다른 경우
#             if len(dp[i - 1][j]) > len(dp[i][j - 1]):  # 위쪽 값이 더 큰 경우
#                 dp[i][j] = dp[i - 1][j]
#             else:  # 왼쪽 값이 더 큰 경우
#                 dp[i][j] = dp[i][j - 1]
