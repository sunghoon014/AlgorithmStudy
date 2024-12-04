import sys

input = sys.stdin.readline

n = int(input())
print(n)

for _ in range(n):
    print(input())
"""
14
push 1
push 2
top
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
top
"""
