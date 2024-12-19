import sys
input = sys.stdin.readline
N = int(input())

vocab = list(set([input().strip() for _ in range(N)]))
vocab.sort(key = lambda x : (len(x), x))

for word in vocab:
    print(word)