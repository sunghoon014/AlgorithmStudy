import sys

input = sys.stdin.read
data = input().splitlines()
n = int(data[0])

A = [ int(num) for num in data[1].split() ]
B = [ int(num) for num in data[2].split() ]

A.sort()
B.sort(reverse=True)

S = 0
for i in range(0, len(A)):
    S += A[i] * B[i]

sys.stdout.write(str(S))