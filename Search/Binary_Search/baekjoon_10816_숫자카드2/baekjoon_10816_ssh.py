import sys

N = int(sys.stdin.readline())
A = dict()
B = list(map(int, sys.stdin.readline().split()))
for i in range(N):
    if B[i] in A:
        A[B[i]] += 1
    else:
        A[B[i]] = 1

M = int(sys.stdin.readline())

result = []
number_to_find = list(map(int, sys.stdin.readline().split()))
for i in range(M):
    if number_to_find[i] in A:
        result.append(A[number_to_find[i]])
    else:
        result.append(0)

print(' '.join(list(map(str, result))))